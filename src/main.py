from ports.inputPort import *
from ports.outputPort import *
import logging
import config as config
from gateway.gateway import Gateway

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

config.loadConfig()
type(config.jsonConfig)

inputPort = InputPort()
outputPort = OutputPort()
gateway = Gateway(inputPort, outputPort)

while (True): pass