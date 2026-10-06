##sum of numbers (1,2,3,4,5)
# sum=0
# i=1
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)    


##sum of those numbers that are divisible by 3 in the range(1,50)
# sum = 0
# i= 1
# while i <= 50:
#     if i % 3 == 0:
#         sum=sum+i
#     i =i+1
# print(sum)


##sum of all 3 digit number
# sum = 0
# num = 100
# while num <= 999:
#     sum += num
#     num += 1
# print("Sum =", sum)



##sum of first 10 even numbers
num = 2
sum= 0
while num< 10:
    sum+= num
    num += 2
print(sum)


#Print each number in a list
l = [12, 30, 34, 78]
for i in l:
    print(i)


#Print each digit in a number   
n = 1234
for i in str(n):
    print(i) 


#Find the sum of elements in a list   
l = [12, 30, 34, 78]
sum = 0
for i in l:
    sum = sum + i
print(sum) 


#Find the sum of digits in a number
n = 1234
sum = 0
for i in str(n):
    sum = sum + int(i)
print(sum)