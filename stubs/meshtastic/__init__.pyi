from typing import *
from . import util as util
from .protobuf import apponly_pb2 as apponly_pb2, channel_pb2 as channel_pb2, config_pb2 as config_pb2
from _typeshed import Incomplete
from datetime import datetime as datetime
from google.protobuf.json_format import MessageToJson as MessageToJson
from meshtastic.node import Node as Node
from meshtastic.util import DeferredExecution as DeferredExecution, Timeout as Timeout, catchAndIgnore as catchAndIgnore, fixme as fixme, stripnl as stripnl
from pubsub import pub as pub
from tabulate import tabulate as tabulate
from typing import NamedTuple

LOCAL_ADDR: str
BROADCAST_NUM: int
BROADCAST_ADDR: str
OUR_APP_VERSION: int
NODELESS_WANT_CONFIG_ID: int
publishingThread: Incomplete

class ResponseHandler(NamedTuple):
    callback: Callable
    ackPermitted: bool = ...

class KnownProtocol(NamedTuple):
    name: str
    protobufFactory: Optional[Callable] = ...
    onReceive: Optional[Callable] = ...

protocols: Incomplete
