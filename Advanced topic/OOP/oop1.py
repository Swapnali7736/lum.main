#define a class named employee with the following details.
#data members:
#empid,name,age,salary,designation,place
#member metjods
#getsalary(),showpersonaldetails()
#create two objects for the employee class and call the above member methods.


class Employee:
    def __init__(self):
        self.empid=input("enter empid:")
        self.name=input("enter name:")
        self.age=int(input("enter age:"))
        self.salary=int(input("enter salary:"))
        self.designation=input("enter designation:")
        self.place=input("enter place:")
    def getsalary(self):
        print(self.salary)
    def showpersonaldetails(self):
        print(self.empid,self.name,self.age,self.designation,self.place)

e=Employee()
e.getsalary()
e.showpersonaldetails()

        


        