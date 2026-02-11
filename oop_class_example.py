class Account: 
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        print(amount, "debited")
        print(self.balance, "total remaining balance")

    def credit(self, amount):
        self.balance += amount
        print(amount, "credited") 
        print(self.balance, "total remaining balance") 

acc1 = Account(29000, 121)  
acc1.debit(9000) 
acc1.credit(1000) 