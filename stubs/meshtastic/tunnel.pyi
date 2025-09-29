from _typeshed import Incomplete
from meshtastic import mt_config as mt_config
from meshtastic.protobuf import portnums_pb2 as portnums_pb2
from meshtastic.util import ipstr as ipstr, readnet_u16 as readnet_u16

def onTunnelReceive(packet, interface) -> None: ...

class Tunnel:
    class TunnelError(Exception):
        message: Incomplete
        def __init__(self, message) -> None: ...
    iface: Incomplete
    subnetPrefix: Incomplete
    udpBlacklist: Incomplete
    tcpBlacklist: Incomplete
    protocolBlacklist: Incomplete
    LOG_TRACE: int
    tun: Incomplete
    def __init__(self, iface, subnet: str = '10.115', netmask: str = '255.255.0.0') -> None: ...
    def onReceive(self, packet) -> None: ...
    def sendPacket(self, destAddr, p) -> None: ...
    def close(self) -> None: ...
