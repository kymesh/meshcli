from _typeshed import Incomplete

class SupportedDevice:
    name: Incomplete
    version: Incomplete
    for_firmware: Incomplete
    device_class: Incomplete
    usb_vendor_id_in_hex: Incomplete
    usb_product_id_in_hex: Incomplete
    baseport_on_linux: Incomplete
    baseport_on_mac: Incomplete
    baseport_on_windows: Incomplete
    def __init__(self, name, version=None, for_firmware=None, device_class: str = 'esp32', baseport_on_linux=None, baseport_on_mac=None, baseport_on_windows: str = 'COM', usb_vendor_id_in_hex=None, usb_product_id_in_hex=None) -> None: ...

tbeam_v0_7: Incomplete
tbeam_v1_1: Incomplete
tbeam_M8N: Incomplete
tbeam_M8N_SX1262: Incomplete
tlora_v1: Incomplete
tlora_v1_3: Incomplete
tlora_v2: Incomplete
tlora_v2_1_1_6: Incomplete
heltec_v1: Incomplete
heltec_v2_0: Incomplete
heltec_v2_1: Incomplete
rak11200: Incomplete
meshtastic_diy_v1: Incomplete
techo_1: Incomplete
rak4631_5005: Incomplete
rak4631_5005_epaper: Incomplete
rak4631_19003: Incomplete
nano_g1: Incomplete
supported_devices: Incomplete
