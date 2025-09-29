import io
import serial
from _typeshed import Incomplete
from meshtastic.mesh_interface import MeshInterface as MeshInterface
from meshtastic.util import is_windows11 as is_windows11, stripnl as stripnl

START1: int
START2: int
HEADER_LEN: int
MAX_TO_FROM_RADIO_SIZE: int

class StreamInterface(MeshInterface):
    stream: serial.Serial | None
    is_windows11: Incomplete
    cur_log_line: str
    def __init__(self, debugOut: io.TextIOWrapper | None = None, noProto: bool = False, connectNow: bool = True, noNodes: bool = False) -> None: ...
    def connect(self) -> None: ...
    def close(self) -> None: ...
