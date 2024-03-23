from connectors.connector import *
from paho.mqtt.client import Client, CallbackAPIVersion
import config as config
from gateway.message import Destination, Message, Source

class MqttClientConnector(Connector):
    def __init__(self, callbacks: List[Callable[[Message], Optional[Message]]], side: SideType) -> None:
        super().__init__(callbacks, side)
        self.client = Client(CallbackAPIVersion.VERSION2)
        
    def start(self):
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(config.jsonConfig["mqttClient"]["url"], config.jsonConfig["mqttClient"]["port"], 60)
        self.client.loop_start()

    # def onReceiveMessage(self, message: Message):
    #     info(f"{__name__} parsed message to {message}")

    # def onRequestMessage(self, message: Message):
    #     self.client.subscribe(f"$SYS/{message.dest}")

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/broker/load/bytes/sent/1min")

    def convertToMessage(self, payload: bytes, address: bytes) -> Message:
        super().convertToMessage(payload, address)
        return Message(payload, Source(f'{config.jsonConfig["mqttClient"]["url"]}:{config.jsonConfig["mqttClient"]["port"]}'), Destination(address), self.side)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        info(f"{__name__} got message {msg.topic}:{msg.payload}")
        self.onReceiveMessage(self.convertToMessage(msg.payload, msg.topic))