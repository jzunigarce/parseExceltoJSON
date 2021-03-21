from abc import ABC, abstractmethod

class ValueTypeInterface(ABC):
    
    @abstractmethod
    def parse(self):
        pass
