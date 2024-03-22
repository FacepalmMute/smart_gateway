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
    def __init__(self, data: bytes, source: Source, destination: Destination) -> None:
        self.data = data
        self.destination = destination
        self.source = source
        pass

    def __str__(self) -> str:
        return f"{self.source} >> {self.data} >> {self.destination}"

