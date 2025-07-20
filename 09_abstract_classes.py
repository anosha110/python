from abc import abstractmethod, ABC

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):

    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        return self.width * self.height
    
rect=Rectangle(4,5)
print(rect.area())