from src.gateway.message import *
from logging import info, debug, warning, error
from abc import ABC, abstractmethod
from typing import List, Callable, Optional

NUMBER_OF_CALLBACKS = 2

class Connector(ABC):
    def __init__(self, callbacks: List[Callable[[Message], Optional[Message]]], side: SideType) -> None:
        assert len(callbacks) == NUMBER_OF_CALLBACKS
        self.onReceiveMessage = callbacks[0]
        self.onRequestMessage = callbacks[1]
        self.side = side

    # @abstractmethod
    # def onReceiveMessage(self, message: Message):
    #     raise Exception("Not supported for this connector")

    # @abstractmethod
    # def onRequestMessage(self, message: Message):
    #     raise Exception("Not supported for this connector")

    @abstractmethod
    def requestMessage(self, address: str) -> Message | None:
        pass

    @abstractmethod
    def convertToMessage(self, payload: bytes, address: bytes) -> Message:
        pass

    @abstractmethod
    def start(self):
        pass