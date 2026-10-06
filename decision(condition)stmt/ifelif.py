#Write a Python program to find the maximum of three number.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("First number is maximum")
elif b > a and b > c:
    print("Second number is maximum")
else:
    print("Third number is maximum")


# Write a Python program to check whether a given number is:
# 1. Divisible by both 2 and 3.
# 2. Divisible by 2 but not by 3.
# 3. Divisible by 3 but not by 2.
# 4. Not divisible by 2 and 3.

n=int(input("enter a number"))
if(n%2==0):
    #print("divisible by 2")
    if(n%3==0):
        print("divisible by 2 and 3")
    else:
        print(" divisible by 2 and not divisible by 3")  
else:
    if n%3==0:
        print(" divisible by 3 and not by 2") 
    else:
        print("not divisible by 2 and 3") 




#Check whether an entered number is 2 digit / 3 digit / 4 digit
num = int(input("Enter a number: "))

if 10 <= num <= 99:
    print("2 digit number")
elif 100 <= num <= 999:
    print("3 digit number")
elif 1000 <= num <= 9999:
    print("4 digit number")
else:
    print("Not a 2, 3 or 4 digit number")


#Write a Python program to perform basic arithmetic operations (+, -, *, /) using two numbers 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")



#Write a Python program to find the number of days in a given month. 
month = input("Enter month name: ")
L1 = ["January", "March", "May", "July", "August", "October", "December"]
L2 = ["April", "June", "September", "November"]
L3 = ["February"]
if month in L1:
    print("31 days")
elif month in L2:
    print("30 days")
elif month in L3:
    print("28 or 29 days")
else:
    print("Invalid month")    
     

#Write a Python program to display the grade of a student based on the entered score.
# 91-100   Grade A
# 81-90    Grade B
# 71-80    Grade C
# 61-70    Grade D
# Below 61 Grade E     
score = int(input("Enter score: "))
if 91 <= score <= 100:
    print("Grade A")
elif 81 <= score <= 90:
    print("Grade B")
elif 71 <= score <= 80:
    print("Grade C")
elif 61 <= score <= 70:
    print("Grade D")
elif score < 61:
    print("Grade E")
else:
    print("Invalid score")