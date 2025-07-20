class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"{self.brand} is started.")

car1=Car("civic")
print(car1.brand)
car1.start()