from abc import ABC, abstractmethod
from src.connectors.connector import Connector
from src.gateway.message import *
from logging import info, debug, warning, error
from queue import Queue
import time

MAX_MESSAGES_IN_QUEUE = 100

class Port(ABC):
    def __init__(self) -> None:
        self.messageQueue = Queue(maxsize=MAX_MESSAGES_IN_QUEUE)
        pass

    def setOtherSide(self, otherSide: 'Port'):
        self.otherSide = otherSide

    def setConnector(self, connector: Connector):
        self.connector = connector
        self.connector.start()

    def onRequest(self, message: Message):
        debug(message)

    def onReceivedMessage(self, message: Message):
        debug(f"onReceivedMessage: {message}")
        self.messageQueue.put(message)

    def onRequestMessage(self, message: Message) -> Message:
        startTime = time.time()
        debug(f"onRequestMessage: {message}")
        address = message.dest.address
        message = self.otherSide.connector.requestMessage(address)
        if message == None:
            # message could not retained from connector directly. Check queue for messages
            debug("Polling for messageQueue...")
            message = self.otherSide.messageQueue.get()
        endTime = time.time()
        info(f"RequestMessage took {round(endTime - startTime, 2)} seconds")
        return message