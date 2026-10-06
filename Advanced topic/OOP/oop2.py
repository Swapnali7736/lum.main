#define a class named Student with the following details:
#Data members:
#sname,rollno,class1,mark1,mark2,mark3
#member methods:
#calculate()-calculates the total and average
#showdetails()- displays the details of a student with average mark
#create one object for the class and call the above member methods.


class Student:
    def __init__(self):
        self.sname=input("enter your name:")
        self.rollno=int(input("enter your rollno:"))
        self.cls=input("enter your class:")
        self.mark1=int(input("enter your mark1:"))
        self.mark2=int(input("enter your mark2:"))
        self.mark3=int(input("enter your mark3:"))
    def calculate(self):
       self.t=self.mark1+self.mark2+self.mark3
    #    print(t)  
       self.avg=(self.t/3)  
    #    print(avg)
        
    def showdetails(self):
        print(self.sname,self.rollno,self.cls,self.t,self.avg)
s=Student()
s.calculate()  
s.showdetails()      


