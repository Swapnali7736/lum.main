##class classname:
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name is:",self.name,"age is:",self.age)

##object creation
##objectname=classname(arguments)

# p=Person("anu",23)  
# p.display()          





# define a class named person.
# accept name and age from the user
# display the details by using show() method
# create an object and call the method


class Person:
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
    def show(self) :
        print(self.name,self.age) 
p=Person() 
p.show()         