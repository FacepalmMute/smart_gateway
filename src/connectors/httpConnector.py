from connectors.connector import *
from gateway.message import Message
import tornado
import asyncio
import config

class HttpConnector(Connector):
    def __init__(self, callbacks: List[Callable[[Message], Optional[Message]]], side: SideType) -> None:
        super().__init__(callbacks, side)
        self.handler = RequestHandler

    async def requestHandler(self) -> None:
        self.server = tornado.web.Application([(r'/(.*)', RequestHandler, dict(httpConnector=self))])
        self.server.listen(config.jsonConfig["http"]["port"])
        await asyncio.Event().wait()

    # def onReceiveMessage(self, message: Message):
    #     info(f"{__name__} parsed message to {message}")

    # def onRequestMessage(self, message: Message):
    #     return super().onRequestMessage(message)

    def convertToMessage(self, payload: bytes, address: bytes) -> Message:
        super().convertToMessage(payload, address)
        return Message(payload, Source(f'{config.jsonConfig["http"]["url"]}:{config.jsonConfig["http"]["port"]}'), Destination(address), self.side)

    def start(self):
        super().start()
        asyncio.run(self.requestHandler())

class RequestHandler(tornado.web.RequestHandler):
    def initialize(self, httpConnector: HttpConnector):
        self.httpConnector = httpConnector

    def get(self, url):
        message = self.httpConnector.convertToMessage("", url)
        self.httpConnector.onRequestMessage(message)  # Hier rufst du onReceiveMessage auf
        self.write("Hello, world")