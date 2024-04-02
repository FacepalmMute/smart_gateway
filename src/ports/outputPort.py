from .port import Port

class OutputPort(Port):
    def __init__(self) -> None:
        super().__init__()

    def askForValueInAddress(self):
        self.connector