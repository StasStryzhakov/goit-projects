from abc import abstractmethod, ABC
import json
import pickle

class SerializationInterface(ABC):
    
    @abstractmethod
    def save_data():
        pass
    
    @abstractmethod
    def load_data():
        pass
    
    
    
    
class JsonSerialize(SerializationInterface):
    
    def save_data(self):
        with open('file.bin', 'wb') as fw:
            json.dump(self.data, fw)
    
    def load_data(self):
        try:
            with open('file.bin', 'rb') as fr:
                self.data = json.load(fr)
        except FileNotFoundError:
            pass
        
class PickleSerialize(SerializationInterface):
    
    def save_data(self):
        with open('file.bin', 'wb') as fw:
            pickle.dump(self.data, fw)
    
    def load_data(self):
        try:
            with open('file.bin', 'rb') as fr:
                self.data = pickle.load(fr)
        except FileNotFoundError:
            pass