class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print(f"{self.name} is saying {self.breed}")

d=Dog("Rex","hello")
d.bark()