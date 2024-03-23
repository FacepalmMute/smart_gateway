from abc import ABC, abstractmethod
from connectors.connector import Connector

class Port(ABC):
    def __init__(self) -> None:
        pass

    def setConnector(self, connector: Connector):
        self.connector = connector
        self.connector.start()