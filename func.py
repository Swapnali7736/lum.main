#Q.Addition of 2 numbers using function

#  function definition
# def addition():
#     "Addition of 2 numbers"
#     num1=int(input("enter num1:"))
#     num2=int(input("enter num2:"))
#     sum=num1+num2
#     print("sum",sum)
#     return
# addition() #function call , execution starts from here 



#Q.define a function to display a message "Hello Your name"

# def namecall():
#     name = input("Enter your name: ")
#     print("Hello " + name)

# # function call
# namecall()



#Q.define a function to print the factorial of a number

# def factorial_num():
#     fact = 1
#     n=int(input("enter the number"))
#     for i in range(1,n+1):
#         fact = fact * i
#     print(fact)  
# factorial_num()



#Q.define a function to find the number of occurence of a particular character in a string

# def count_char():
#     s = input("Enter a string: ")
#     ch = input("Enter a character: ")
#     count = 0
#     for i in s:
#         if i == ch:
#             count = count + 1
#     print("Occurrences:", count)
# # Function call
# count_char()



#Q.define a function to print the sum of elements in a  list l=[89,45,67,12]

# def list_sum():
#     l = [89, 45, 67, 12]
#     sum = 0
#     for i in l:
#         sum = sum + i
#     print("Sum is:", sum)

# # Function call
# list_sum()


#Q.check whether a number is prime or not using function

# def prime():
#     num = int(input("Enter a number: "))
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# prime()



#Q.Define a function that takes three arguments (amount,rate,year) and finds the simple interest value.

# def simple_interest(amount, rate, year):
#     s = (amount * rate * year) / 100
#     print("Simple Interest:", s)

# # Function call
# simple_interest(20000, 5, 2)



#Q.Define a function and calculate the product of 3 numbers

# def product(a, b, c):
#     p = a * b * c
#     return p
# # Function call
# result = product(2, 3, 4)
# print("Product:", result)



#Q.Define a function that counts the number of occurrences of a given character in a string.

# def count_char(s, ch):
#     count = 0
#     for i in s:
#         if i == ch:
#             count = count + 1
#     return count
# # Function call
# result = count_char("hii ", "i")
# print("Occurrences:", result)


#Q.define a function that takes list as argument and returns a new list containing unique elements from list.

# def unique_list(l):
#     new = []
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# l= [12, 34, 78, 12, 67, 34, 90, 90, 23]
# result = unique_list(l)
# print(result)



# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]

#Q.define a function that takes list as argument and returns a new list containing common elements from list.

# def common_elements(l1,l2):
#     for i in l1:
#         if i in l2:
#             print(i)
#     return        

# common_elements(list1,list2)


#sum using arbitary positional argument
def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(sum(2,6,8,9)) 
print(sum(21,16,8,49))       