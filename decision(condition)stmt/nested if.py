# Write a Python program to check whether an entered number is:
# 1. Positive even
# 2. Positive odd
# 3. Negative even
# 4. Negative odd
# using nested if statements.

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    if num % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")