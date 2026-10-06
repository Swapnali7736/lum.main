#ARMSTRONG NUMBER

# num = input("Enter a number: ")
# sum = 0
# l = len(num)
# for i in num:
#     sum = sum + int(i) ** l
# if sum == int(num):
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")


#FIBINOCCI SERIES    

a = 0
b = 1
for i in range(1, 11):
    print(a)
    a, b = b, a + b


# #FACTORS OF A NUMBER

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)    


# #Create a list of 5 number 
   
# num_list = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     num_list.append(num)
# print(num_list)   


# #Create a list of 5 random numbers 

# import random
# num_list = []
# for i in range(5):
#     num = random.randint(1, 100)
#     num_list.append(num)
# print(num_list)