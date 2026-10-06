#1) Program to check whether a number is Prime or Not

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Number is neither prime nor composite")


#2) Program to check whether a number is Perfect Number or Not    

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")