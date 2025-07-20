class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value<0:
            print("price cannot be negative")
        else:
            self._price=value

    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

product=Product("iphone",500000)
print(product.price)
product.price = -1000

del product.price