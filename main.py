from ports.inputPort import *
from ports.outputPort import *
from connectors.mqttClientConnector import MqttClientConnector
from connectors.httpConnector import HttpConnector
import logging
import config
from gateway.gateway import Gateway

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

config.loadConfig()
type(config.jsonConfig)

inputPort = InputPort(MqttClientConnector())
outputPort = OutputPort(HttpConnector())
gateway = Gateway(inputPort, outputPort)

while (True): pass