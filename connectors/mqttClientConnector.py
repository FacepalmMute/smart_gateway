from connectors.connector import *
from paho.mqtt.client import Client, CallbackAPIVersion
from gateway.message import *
import config

class MqttClientConnector(Connector):
    def __init__(self) -> None:
        super().__init__()
        self.client = Client(CallbackAPIVersion.VERSION2)
        
    def start(self):
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(config.jsonConfig["mqttClient"]["url"], config.jsonConfig["mqttClient"]["port"], 60)
        self.client.loop_start()

    def onReceiveMessage(self, message: Message):
        super().onReceiveMessage(message)
        info(f"{__name__} parsed message to {message}")

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        info(f"{__name__} got message {msg}")
        message = Message(msg.payload, Source(f'{config.jsonConfig["mqttClient"]["url"]}:{config.jsonConfig["mqttClient"]["port"]}'), Destination(msg.topic))
        self.onReceiveMessage(message)