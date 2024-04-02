from src.connectors.connector import *
from src.gateway.message import Message
import tornado
import src.config as config
from threading import Thread

class HttpConnector(Connector):
    def __init__(self, callbacks: List[Callable[[Message], Optional[Message]]], side: SideType) -> None:
        super().__init__(callbacks, side)
        self.handler = RequestHandler

    def requestHandler(self) -> None:
        self.server = tornado.web.Application([(r'/(.*)', RequestHandler, dict(httpConnector=self))])
        self.server.listen(config.jsonConfig["http"]["port"])
        tornado.ioloop.IOLoop.current().start()

    def convertToMessage(self, payload: bytes, address: bytes) -> Message:
        super().convertToMessage(payload, address)
        return Message(payload, Source(f'{config.jsonConfig["http"]["url"]}:{config.jsonConfig["http"]["port"]}'), Destination(address), self.side, ProtocolType.HTTP)

    def start(self):
        super().start()
        self.thread = Thread(target=self.requestHandler)
        self.thread.daemon = True  # For clearer quit
        self.thread.start()

    def requestMessage(self, address: str) -> Message | None:
        pass

class RequestHandler(tornado.web.RequestHandler):
    def initialize(self, httpConnector: HttpConnector):
        self.httpConnector = httpConnector

    def get(self, url):
        message = self.httpConnector.convertToMessage("", url)
        message = self.httpConnector.onRequestMessage(message)  # Hier rufst du onReceiveMessage auf
        self.write(message.data)