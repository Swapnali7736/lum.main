#Write a Python program to display a number 
num = int(input("Enter a number: "))
print(num)


# Write a Python program to display a number if the entered number is even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num)


# Write a Python program to display a number if the entered number is positive.
num = int(input("Enter a number: "))
if num > 0:
    print(num)


# Write a Python program to display a number if the entered number is divisible by 3.
num = int(input("Enter a number: "))
if num % 3 == 0:
    print(num)


# Write a Python program to display a number if the entered number is divisible by both 3 and 5.    
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num)


# Write a Python program to display a name if the entered name contains the letter 'n'.   
name = input("Enter a name: ")
if "n" in name:
    print(name) 


# Write a Python program to display a name if the entered name starts with the letter 'n'.
name = input("Enter a name: ")
if name[0] == "n":
    print(name)


# Write a Python program to display a location name if the entered location contains the word 'land'.    
location = input("Enter a location: ")
if "land" in location:
    print(location)