import socket
from _typeshed import Incomplete
from meshtastic.stream_interface import StreamInterface as StreamInterface

DEFAULT_TCP_PORT: int

class TCPInterface(StreamInterface):
    stream: Incomplete
    hostname: str
    portNumber: int
    socket: socket.socket | None
    def __init__(self, hostname: str, debugOut=None, noProto: bool = False, connectNow: bool = True, portNumber: int = ..., noNodes: bool = False) -> None: ...
    def myConnect(self) -> None: ...
    def close(self) -> None: ...
