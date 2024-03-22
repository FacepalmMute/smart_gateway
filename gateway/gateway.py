from ports.inputPort import InputPort
from ports.outputPort import OutputPort



class Gateway():
    def __init__(self, inputPort: InputPort, outputPort: OutputPort):
        self.inputPort = inputPort
        self.outputPort = outputPort