from src.connectors.connector import *
from paho.mqtt.client import Client, CallbackAPIVersion
import src.config as config
from src.gateway.message import Destination, Message, Source

class MqttClientConnector(Connector):
    def __init__(self, callbacks: List[Callable[[Message], Optional[Message]]], side: SideType) -> None:
        super().__init__(callbacks, side)
        self.client = Client(CallbackAPIVersion.VERSION2)

    def start(self):
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(config.jsonConfig["mqttClient"]["url"], config.jsonConfig["mqttClient"]["port"], 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, reason_code, properties):
        # info(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/broker/load/bytes/sent/1min")
        pass

    def convertToMessage(self, payload: bytes, address: bytes) -> Message:
        super().convertToMessage(payload, address)
        return Message(payload, Source(f'{config.jsonConfig["mqttClient"]["url"]}:{config.jsonConfig["mqttClient"]["port"]}'), Destination(address), self.side, ProtocolType.MQTT)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        info(f"{__name__} got message {msg.topic}:{msg.payload}")
        self.onReceiveMessage(self.convertToMessage(msg.payload, msg.topic))
        self.client.unsubscribe(msg.topic)

    def requestMessage(self, address: str) -> Message | None:
        self.client.subscribe(address)
        return None