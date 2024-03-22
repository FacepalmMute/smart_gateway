from connector import Connector
from mqttBrokerConnector import MqttBrokerConnector
from mqttClientConnector import MqttClientConnector

class MqttConnector(Connector):
    def __init__(self) -> None:
        super().__init__()
        self.client = MqttBrokerConnector()
        self.client = MqttClientConnector()