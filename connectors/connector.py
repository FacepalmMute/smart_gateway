from gateway.message import *
from logging import info, debug, warning, error
from abc import ABC, abstractmethod

class Connector(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def onReceiveMessage(self, message: Message):
        pass

    @abstractmethod
    def start(self):
        pass