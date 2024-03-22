from connectors.connector import *
from gateway.message import Message

class HttpConnector(Connector):
    def __init__(self) -> None:
        super().__init__()

    def onReceiveMessage(self, message: Message):
        return super().onReceiveMessage(message)

    def start(self):
        return super().start()