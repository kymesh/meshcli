from _typeshed import Incomplete
from meshtastic.stream_interface import StreamInterface as StreamInterface

class SerialInterface(StreamInterface):
    noProto: Incomplete
    devPath: str | None
    stream: Incomplete
    def __init__(self, devPath: str | None = None, debugOut=None, noProto: bool = False, connectNow: bool = True, noNodes: bool = False) -> None: ...
    def close(self) -> None: ...
