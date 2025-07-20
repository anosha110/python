def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator"
    cls.greet=greet
    return cls
@add_greeting
class person:
     def __init__(self,name):
         self.name=name

     def introduce(self):
         return (f"Hi i am {self.name}")

person=person("Ali")
print(person.greet())
         