# api for meshtastic cli
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import time
import sys


class MeshConn:
    def __init__(self, on_message_callback=None):
        """
        Connect to a meshtastic radio through a serial port.
        """
        self.on_message_callback = on_message_callback
        pub.subscribe(self.on_receive, "meshtastic.receive")

        try:
            self.interface = meshtastic.serial_interface.SerialInterface()
        except Exception as e:
            print("ERROR: There was an error connecting to the radio.", e)
            sys.exit(1)

        try:
            self.nodes = self.interface.nodes.items()
        except AttributeError as e:
            print("ERROR: It is likely that there is no radio connected.", e)
            sys.exit(1)

        self.this_node = self.interface.getMyNodeInfo()
        
        # create dictionary for long names and radio ids {"longName":"id"}
        self.name_id_map = { metadata['user']['longName'] : id for id, metadata in self.nodes}

        # another one for the reverse {"id": "longName"}
        self.id_name_map = { id : metadata['user']['longName'] for id, metadata in self.nodes}

    
    def on_receive(self, packet, interface):
        """
        Receive a message sent to our radio.
        """
        try:
            to_id = packet.get("toId")
            from_id = packet.get("fromId")
            message = packet["decoded"]["text"]
            this_id = self.this_node['user']['id']

            if to_id == this_id or to_id == "^all":
                sender_name = self.id_name_map.get(from_id, "Unknown")
                if self.on_message_callback:
                    self.on_message_callback(sender_name, message)
        except Exception as e:
            print(f"[ERROR on_receive] {e}")


    def get_long_names(self):
        """
        Retrieve the names of all other nodes in the mesh
        """
        long_names = self.name_id_map.keys()
        return long_names
    
    async def send_message(self, longname: str, message: str):
        id = self.name_id_map[longname]
        self.interface.sendText(message, destinationId=id)

