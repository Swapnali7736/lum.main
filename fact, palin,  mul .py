##factorial of a number

num=int(input("enter a number"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1
print(fact)    




##print multiplication table of a number

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "*", i, "=", num * i)
    i += 1


## palindrome

count = 0
num = 1

while num <= 1000:
    if str(num) == str(num)[::-1]:
        print(num)
        count=count+1
    num=num+1

print(count)    