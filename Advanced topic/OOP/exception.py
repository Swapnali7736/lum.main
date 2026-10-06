#sum of 2 numbers
# try:
#     n1=int(input("enter the number:"))
#     n2=int(input("enter the number:"))
#     r=n1/n2
#     print(r)
# except:
#     print("Zero Division error")    

# #optional
# else:
#     print("no exception in normal block") 
# finally:
#     print("Finished")   



# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# negative number/character input

# import math
# try:
#     n = int(input("Enter a number: "))
#     fact = math.factorial(n)
#     print("Factorial =",fact)

# except:
#     print("Invalid input")
# #optional   
# else:
#     print("Factorial",fact)    
    
    
    
# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

try:
    num1=float(input("Enter number:"))
    num2=float(input("Enter number:"))
    op=input("Enter operator:")
    ch=int(input("enter the choice"))
    if ch==1:
        print(num1+num2)
    elif ch==2:
        print(num1-num2)
    elif ch==3:
        print(num1*num2)
    elif ch==4:
        print(num1/num2)
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("ZeroDivisionError")

except ValueError:
    print("Value Error occurs")

except:
    print("Invalid input")    



# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist        

# try:
#     file_name = input("Enter the file name: ")
#     f = open(file_name, "r")
#     print(f.read())
#     f.close()

# except FileNotFoundError:
#     print("File does not exist")