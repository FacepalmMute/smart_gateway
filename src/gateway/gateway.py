from src.ports import InputPort, OutputPort
from src.connectors import *
from src.gateway.message import *
import src.config as config 
from logging import info, debug, warning, error

class Gateway():
    def __init__(self, leftPort: InputPort, rightPort: OutputPort):
        self.leftPort = leftPort
        self.rightPort = rightPort

        self.leftPort.setOtherSide(self.rightPort)
        self.rightPort.setOtherSide(self.leftPort)

        debug(f"Created gateway")
        self.callbacksLeft = [self.leftPort.onReceivedMessage, self.leftPort.onRequestMessage]
        self.callbacksRight = [self.rightPort.onReceivedMessage, self.rightPort.onRequestMessage]

    def setConnector(self, side: SideType, connector: Connector):
        if side == SideType.LEFTSIDE:
            self.leftPort.setConnector(connector(self.callbacksLeft, side))
            debug("Leftside connector initialized")
        elif side == SideType.RIGHTSIDE:
            self.rightPort.setConnector(connector(self.callbacksRight, side))
            debug("Rightside connector initialized")
        else:
            raise Exception("Invalid side. Can only be right or left")

