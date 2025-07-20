class Multiplier:
    def __init__(self,factor):
        self.factor=factor

    def __call__(self,number):
        return number * self.factor
    
multi=Multiplier(5)
print(callable(Multiplier))

result=multi(10)
print(result)