class bank:
    bank_name="UBL Bank"

    @classmethod
    def change_name(cls,name):
        cls.bank_name=name

b1=bank()
print(b1.bank_name)
bank.change_name("HBL")
print(b1.bank_name)