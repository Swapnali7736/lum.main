#define a class book with the following details.
#data members
#bookname,bookid,authorid,authorname,price,booktitle
#member methods
#getauthorid(),getauthorname(),getbooktitle(),getprice()
#setauthorid,setauthorname(),setbooktitle(),setprice()


class Book:
    def __init__(self):
        self.bname=input("enter the bname:")
        self.bid=input("enter the bid:")
        self.aid=input("enter the aid:")
        self.aname=input("enter the aname:")
        self.price=int(input("enter the price:"))
        self.btitle=input("enter the booktitle:")
    def getauthorid(self):
        print(self.aid)
    def getauthorname(self):
        print(self.aname)   
    def getbooktitle(self):
        print(self.btitle) 
    def getprice(self):
        print(self.price) 
    def setauthorid(self):
        self.aid=input("enter new authorid:")
        self.getauthorid()
    def setauthorname(self):
        self.aname=input("enter the new author name:") 
        self.getauthorname()
    def setbooktitle(self):
        self.btitle=input("enter the new book title:")
        self.getbooktitle()
    def setprice(self):
        self.price=int(input("enter the new price:"))  
        self.getprice()      
b=Book()
b.setauthorid()
b.setauthorname()
b.setbooktitle()
b.setprice()        


