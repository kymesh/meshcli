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

    
    def on_connection(self, interface, topic=pub.AUTO_TOPIC):
        print("Connected to mesh")


    def get_long_names(self):
        """
        Retrieve the names of all other nodes in the mesh.
        Takes like 10s to run for > 300 nodes lol.
        """
        metadata = self.nodes.values()
        long_names = [ node['user']['longName'] for node in metadata]
        
        return long_names

