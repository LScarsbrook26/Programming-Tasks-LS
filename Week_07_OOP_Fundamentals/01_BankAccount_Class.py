"""
TASK: 01 Bankaccount Class

# Skills - https://www.w3schools.com/python/python_oop.asp Highly recommend you visit this site.
Create class with the following attributes:
- Owner
- Balance
- Log
With the following methods:
- deposit()
- withdraw() with validation or an overdraft validation
- get_balance()
- get_log() of all transactions

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
class people:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("your balance is now:", self.balance)
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            ("not enough")
        else:
            ("valid")
            self.balance -= amount
            print("your balance is now:", self.balance)
        return self.balance
    
    def getBalance(self):
        print(self.balance)
    
    def getLog():
        

name = input("enter name")
account = int(input("enter balance"))
p1 = people(name, account)
while true:
    print(" 1. deposit, 2. withdraw, 3. getBalance, 4. getLog")
    num = int(input())
    if num == 1:
        amount = int(input("enter how much to add"))
        p1.deposit(amount)
    elif num == 2:
        amount = int(input("enter how much to take out"))
        p1.withdraw(amount)
    elif num == 3:
        p1.getBalance
    elif num == 4:
        p1.getLog
    else:
        ("not valid")
