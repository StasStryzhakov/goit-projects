from abc import abstractmethod, ABC
import json

class SerializationInterface(ABC):
    
    @abstractmethod
    def save_data():
        pass
    
    @abstractmethod
    def load_data():
        pass
    
    
    
    
class SomeDict(SerializationInterface):
    
    def save_data(self):
        with open('file.bin', 'wb') as fw:
            json.dump(self.data, fw)
    
    def load_data(self):
        try:
            with open('file.bin', 'rb') as fr:
                self.data = json.load(fr)
        except FileNotFoundError:
            pass