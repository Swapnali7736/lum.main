#write a menu driven python program for a banking system using a class
#Account to perform the following operations:
#1.create an account
#2.withdraw money
#3.deposit money
#4.display balance
#5.exit

#store account details in a list and search accounts using the account number
#display "account not found" if the account does not exist.


class Account:
    def __init__(self):
        self.ano=int(input("enter the acccount number:"))
        self.aname=input("enter the acccount name:")
        self.balance=int(input("enter the balance:"))
    def withdraw(self):
        amt=int(input("enter the amt to withdraw:"))
        self.balance=self.balance-amt
        print(self.balance) 
        self.showbalance() 
    def deposit(self):
        amt=int(input("enter the amt to deposit:"))    
        self.balance=self.balance+amt
        print(self.balance)
        self.showbalance()
    def showbalance(self):
        print(self.balance)    
l=[]
while(1):
    print("Menu driven program")
    print("1.Create an Account")
    print("2.Withdraw money")
    print("3.Deposit money")
    print("4.Display balance")
    print("5.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        a=Account()
        l.append(a)
    elif ch==2:
        num=int(input("enter your account number:"))
        for i in l:
            if(i.ano==num):
                i.withdraw()
                break
        else:
            print("Account not found")
    elif ch==3:
        num=int(input("enter your account number:"))
        for i in l:
            if(i.ano==num):
                i.deposit()
                break
        else:
            print("Account not found")
    elif ch==4:
        num =int(input("enter your account number:"))
        for i in l:
            if(i.ano==num):
                i.showbalance()
                break
        else:
            print("Account not found")
       
    else:
        exit()