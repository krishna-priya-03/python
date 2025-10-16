class bankaccount():
    def __init__(self, acconame, accotype, accono, accobaln):
        self.accountno = accono
        self.accountname = acconame
        self.accounttype = accotype
        self.accountbalance = accobaln
        self.balance = accobaln  

    def deposit(self, amount):
        self.accountbalance += amount  
        print("current balance =", self.accountbalance)
        print("deposited amount:", amount)

    def accountinfo(self):
        print("accountname is", self.accountname)
        print("accounttype is", self.accounttype)
        print("accountbalance is", self.accountbalance)
        print("accountno is", self.accountno)

    def withdraw(self, amount):
        if amount > self.accountbalance:
            print("insufficient balance!")
        else:
            self.accountbalance -= amount
            print("withdrawn:", amount, "remaining balance", self.accountbalance)


name = input("enter the account name: ")
num = int(input("enter the account number: "))
baln = float(input("enter the account balance: "))
typ = input("enter the account type: ")


obj = bankaccount(name, typ, num, baln)

print("account information is")
obj.accountinfo()


deposit = int(input("enter the amount to be deposited: "))
obj.deposit(deposit)


withdraw = int(input("enter the amount to be withdrawn: "))  
obj.withdraw(withdraw)


option = int(input("enter the option: "))  

if option == 1:
          
    obj.accountinfo()

elif option == 2:
    
    deposit = int(input("enter the amount to be deposited: "))
    obj.deposit(deposit)
else:
    print("valid option..")
