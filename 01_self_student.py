class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Studen Name: {self.name} marks: {self.marks}")

c1=student("Anosha",80)
c1.display()