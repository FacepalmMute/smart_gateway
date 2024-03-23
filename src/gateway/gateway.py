from ports.inputPort import InputPort
from ports.outputPort import OutputPort
from connectors.mqttClientConnector import MqttClientConnector
from connectors.httpConnector import HttpConnector
from gateway.message import *
from logging import info, debug, warning, error

class Gateway():
    def __init__(self, leftPort: InputPort, rightPort: OutputPort):
        self.leftPort = leftPort
        self.rightPort = rightPort

        callbacks = [self.onReceivedMessage, self.onRequestMessage]
        self.leftPort.setConnector(MqttClientConnector(callbacks, SideType.LEFTSIDE))
        self.rightPort.setConnector(HttpConnector(callbacks, SideType.RIGHTSIDE))

    def onReceivedMessage(self, message: Message):
        debug(f"onReceivedMessage: {message}")

    def onRequestMessage(self, message: Message) -> Message:
        debug(f"onRequestMessage: {message}")
