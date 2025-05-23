# api for meshtastic cli
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import time


class MeshConn:
    def __init__(self):
        """
        Connect to a meshtastic radio through a serial port.
        """
        pub.subscribe(self.on_connection, "meshtastic.connection.established")

        self.interface = meshtastic.serial_interface.SerialInterface()
        self.nodes = self.interface.nodes
        
        # create dictionary for long names and radio ids {"longName":"id"}
        self.name_id_map = { metadata['user']['longName'] : id for id, metadata in self.nodes.items()}

    
    def on_connection(self, interface, topic=pub.AUTO_TOPIC):
        print("Connected to mesh")


    def get_long_names(self):
        """
        Retrieve the names of all other nodes in the mesh.
        Takes like 10s to run for > 300 nodes lol.
        """
        long_names = self.name_id_map.keys()
        return long_names
    
    async def send_message(self, longname: str, message: str):
        id = self.name_id_map[longname]
        self.interface.sendText(message, destinationId=id)

