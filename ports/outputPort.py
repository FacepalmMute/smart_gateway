from ports.port import Port
from connectors.connector import Connector

class OutputPort(Port):
    def __init__(self, connector: Connector) -> None:
        super().__init__(connector)
        self.connector.start()