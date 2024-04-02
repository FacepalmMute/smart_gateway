from enum import Enum

class SideType(Enum):
    LEFTSIDE = 0
    RIGHTSIDE = 1

class ProtocolType(Enum):
    HTTP = 0
    MQTT = 1

class Destination():
    def __init__(self, address: str) -> None:
        self.address = address

    def __str__(self) -> str:
        return self.address

class Source():
    def __init__(self, address: str) -> None:
        self.address = address

    def __str__(self) -> str:
        return self.address

class Message():
    def __init__(self, data: bytes, source: Source, dest: Destination, side: SideType, protocol: ProtocolType) -> None:
        self.data = data
        self.dest = dest
        self.source = source
        self.side = side
        self.protocol = protocol

    def __str__(self) -> str:
        return f"{self.side} : {self.source} >> {self.data} >> {self.dest}"

