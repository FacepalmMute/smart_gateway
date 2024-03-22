from abc import ABC, abstractmethod
from connectors.connector import Connector

class Port(ABC):
    def __init__(self, connector: Connector) -> None:
        self.connector = connector