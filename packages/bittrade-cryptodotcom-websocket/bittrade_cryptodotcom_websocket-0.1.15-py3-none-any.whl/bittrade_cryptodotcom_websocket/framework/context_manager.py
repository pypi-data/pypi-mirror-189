import multiprocessing
from contextlib import contextmanager
from dataclasses import dataclass
from logging import getLogger
from typing import Any, Callable, Literal, NamedTuple, Optional, cast

import requests
from ccxt import cryptocom
from elm_framework_helpers.ccxt.models.orderbook import Orderbook
from reactivex import Observable, operators
from reactivex.abc import DisposableBase
from reactivex.disposable import CompositeDisposable
from reactivex.operators import flat_map, share
from reactivex.scheduler import ThreadPoolScheduler
from reactivex.subject import BehaviorSubject

from bittrade_cryptodotcom_websocket import (
    CryptodotcomResponseMessage,
    EnhancedWebsocket,
    EnhancedWebsocketBehaviorSubject,
    exclude_response_messages,
    keep_messages_only,
    keep_new_socket_only,
    keep_response_messages_only,
    private_websocket_connection,
    public_websocket_connection,
    subscribe_open_orders,
    subscribe_order_book,
)
from bittrade_cryptodotcom_websocket.models import (
    CryptodotcomRequestMessage,
    UserBalance,
)
from bittrade_cryptodotcom_websocket.rest import (
    cancel_all_factory,
    cancel_all_http_factory,
    cancel_order_factory,
    close_position_factory,
    close_position_http_factory,
    create_order_factory,
    get_user_balance_factory,
    get_user_open_orders_factory,
)

from ..models.order import OrderDict

logger = getLogger(__name__)


class BookConfig(NamedTuple):
    pair: str
    depth: int


@dataclass
class CryptodotcomContext:
    all_subscriptions: CompositeDisposable
    books: dict[str, Observable[Orderbook]]
    cancel_all: Callable[[str, Literal["trigger", "limit", "all"]], Observable[bool]]
    cancel_all_http: Callable[
        [str, Literal["trigger", "limit", "all"]], Observable[bool]
    ]
    cancel_order: Callable[[str, bool | None, bool | None], Observable[bool]]
    close_position: Callable[
        [str, Literal["market", "limit"], Optional[str]], Observable[int]
    ]
    close_position_http: Callable[
        [str, Literal["market", "limit"], Optional[str]], Observable[int]
    ]
    create_order: Callable[
        [str, str, str, float, Optional[float], Optional[Any]],
        Observable[dict[str, Any]],
    ]
    exchange: cryptocom
    feed_messages: Observable[CryptodotcomResponseMessage]
    get_user_balance: Callable[[], Observable[list[UserBalance]]]
    get_user_open_orders: Callable[[Optional[str]], Observable[list[OrderDict]]]
    guaranteed_websocket: Observable[EnhancedWebsocket]
    private_messages: Observable[CryptodotcomResponseMessage]
    public_messages: Observable[CryptodotcomResponseMessage]
    response_messages: Observable[CryptodotcomResponseMessage]
    scheduler: ThreadPoolScheduler
    websocket_bs: EnhancedWebsocketBehaviorSubject
    open_orders: Observable[Any]
    open_orders_reloaded: Observable[Any]


@contextmanager
def cryptodotcom_sockets(
    add_token: Callable[
        [Observable[CryptodotcomResponseMessage]],
        Callable[[EnhancedWebsocket], Observable[EnhancedWebsocket]],
    ],
    add_token_http: Callable[[requests.models.Request], requests.models.Request],
    books: Optional[tuple[BookConfig]] = None,
):
    books = books or cast(tuple[BookConfig], ())
    exchange = cryptocom()
    exchange.load_markets()
    optimal_thread_count = multiprocessing.cpu_count()
    pool_scheduler = ThreadPoolScheduler(optimal_thread_count)
    all_subscriptions = CompositeDisposable()
    # Set up sockets
    public_sockets = public_websocket_connection()
    private_sockets = private_websocket_connection()

    public_messages = public_sockets.pipe(keep_messages_only(), share())
    private_messages = private_sockets.pipe(keep_messages_only(), share())

    authenticated_sockets = private_sockets.pipe(
        keep_new_socket_only(),
        flat_map(add_token(private_messages)),
        share(),
    )
    response_messages = private_messages.pipe(keep_response_messages_only(), share())
    feed_messages = private_messages.pipe(exclude_response_messages(), share())

    book_observables = {}
    for pair, depth in books or ():
        book_observables[f"{pair}_{depth}"] = public_sockets.pipe(
            keep_new_socket_only(),
            subscribe_order_book(pair, str(depth), public_messages),  # type: ignore
            share(),
        )

    socket_bs: EnhancedWebsocketBehaviorSubject = BehaviorSubject(
        cast(EnhancedWebsocket, None)
    )
    authenticated_sockets.subscribe(socket_bs)
    guaranteed_socket = socket_bs.pipe(
        operators.filter(lambda x: bool(x)),
    )
    get_user_open_orders = get_user_open_orders_factory(response_messages, socket_bs)
    open_orders = guaranteed_socket.pipe(
        subscribe_open_orders(private_messages), share()
    )
    open_orders_reloaded = open_orders.pipe(flat_map(lambda _: get_user_open_orders()))

    context = CryptodotcomContext(
        all_subscriptions=all_subscriptions,
        books=book_observables,
        cancel_all=cancel_all_factory(
            response_messages, open_orders, exchange, socket_bs
        ),
        cancel_all_http=cancel_all_http_factory(add_token_http),
        cancel_order=cancel_order_factory(private_messages, socket_bs),
        close_position=close_position_factory(response_messages, exchange, socket_bs),
        close_position_http=close_position_http_factory(add_token_http),
        create_order=create_order_factory(private_messages, exchange, socket_bs),
        exchange=exchange,
        feed_messages=feed_messages,
        get_user_balance=get_user_balance_factory(response_messages, socket_bs),
        get_user_open_orders=get_user_open_orders,
        guaranteed_websocket=guaranteed_socket,
        open_orders_reloaded=open_orders_reloaded,
        open_orders=open_orders,
        private_messages=private_messages,
        public_messages=public_messages,
        response_messages=response_messages,
        scheduler=pool_scheduler,
        websocket_bs=socket_bs,
    )

    all_subscriptions.add(
        cast(DisposableBase, public_sockets.connect(scheduler=pool_scheduler))
    )
    all_subscriptions.add(
        cast(DisposableBase, private_sockets.connect(scheduler=pool_scheduler))
    )
    yield context

    all_subscriptions.dispose()
