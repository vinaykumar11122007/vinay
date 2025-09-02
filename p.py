class Bank:
    def __init__(self,name,account,balance):
        self.name=name
        self.account=account
        self.balance=balance
    def display(self):
        print("Name:",self.name)
        print("accountnumber:",self.account)
        print("Balance:",self.balance)
        print("-"*30)
m1 = Bank("Vinay",123,5000)
m2 = Bank("Vijay",122,1000)
m3 = Bank("Vikay",133,4000)
m1.display()
m2.display()
m3.display()




