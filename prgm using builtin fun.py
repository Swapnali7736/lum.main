# #Q.Write a program to find the position of a character in a string

# s = "easy programming"
# ch = input("Enter character: ")
# print(s.index(ch))


# #Q.write a program to find the count of character in  a string

# s = "python programming"
# ch = input("Enter character: ")
# print(s.count(ch))


# # #Q.create a random 5 digit otp number and print otp number

# import random
# otp = random.randint(10000, 99999)
# print(otp)


# #Q.create a list of  5 random 3 digit numbers

# import random
# l = []
# for i in range(5):
#     num = random.randint(100, 999)
#     l.append(num)
# print(l)


# #Q.create a dictionary where keys are words and values are length of each word from the string
# s="python coding is easy and fun"

# s = "python coding is easy and fun"
# d = {}
# for i in s.split():
#     d[i] = len(i)
# print(d)


# #Q.create a dictionary where keys are each character and values are number of occurence of each character
# s="hello world"

# s = "hello world"
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)


# #Q.write a program to find the number of digits,letters,and spaces in a string
# s="sdfghjk3456789  dffghjkl345678"

s = "sdfghjk3456789  dffghjkl345678"
letters = 0
digits = 0
spaces = 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)


# #Q. Given a list l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# # # create a list of salaries

# l = [['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# salary = []
# for i in l:
#     salary.append(i[2])
# print(salary)


# # # find the maximum salary
# l = [['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# salary = []
# for i in l:
#     salary.append(i[2])
# print(max(salary))


# # # find minimum salary
# l = [['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# salary = []
# for i in l:
#     salary.append(i[2])
# print(min(salary))


#Q.Given a dictionary d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
# create a new list of students whose mark>=40

# d = {'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
# new = []
# for i in d:
#     if d[i] >= 40:
#         new.append(i)
# print(new)



#Q.Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# Find Common elements

# l1 = [11,27,34,45,56]
# l2 = [27,34,86,91]
# common = []
# for i in l1:
#     if i in l2:
#         common.append(i)
# print(common)



#Q.Given l=23,45,67,12,90,56]
#find second largest number 
# l = [23,45,67,12,90,56]
# l.sort()
# print(l[-2])


#find second smallest number
# l = [23,45,67,12,90,56]
# l.sort()
# print(l[1])