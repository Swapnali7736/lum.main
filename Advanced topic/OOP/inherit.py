#single level inheritance
# class Person:
#     def __init__(self):
#         self.name=input("enter the name:")
#         self.age=int(input("enter the age:"))
#     def showdetails(self):
#         print("name:",self.name,"age:",self.age)  

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter the roll no:"))
#     def studentdetails(self):
#         super().showdetails()
#         print("rollno:",self.rollno) 

# s=Student()
# s.studentdetails()









class Company:
    def __init__(self):
        self.cname=input("enter the cname:")
    def showdetails(self):
        print("name:",self.cname) 
class Employee(Company):
    def __init__(self):
        super().__init__() 
        self.empid=input("enter the empid:") 
        self.designation=input("enter the designation:")
        self.salary=int(input("enter the salary:")) 
    def getsalary(self):
        print("empid:",self.empid,"salary:",self.salary)           

    def showemployeedetails(self): 
        super().showdetails()
        print("empid:",self.empid,"designation:",self.designation,"salary:",self.salary)   

e=Employee()
e.getsalary()
e.showemployeedetails()        