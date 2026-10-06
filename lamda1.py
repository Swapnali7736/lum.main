# #square of a number
# sq=lambda x:x**2
# print(sq(4))


# #cube of a number
# cube=lambda x:x**3
# print(cube(4))

# #square root of a number
# sqrt=lambda x:x**0.5
# print(sqrt(16))

# # Length of a string
# s = lambda x: len(x)
# print(s("hello"))      # Output: 5


# # Name attribute of a dictionary
# name = lambda a: a["name"]
# print(name({"name": "Anu", "age": 23}))   # Output: Anu


# # First character of a string
# first = lambda a: a[0]
# print(first("Python"))    # Output: P


# # Last element of a list
# last = lambda a: a[-1]
# print(last([10, 20, 30, 40]))   # Output: 40


# # Sum of 2 numbers
# sum = lambda x, y: x + y
# print(sum(10, 20))    # Output: 30


# # Sum of 3 numbers
# sum = lambda x, y, z: x + y + z
# print(sum(10, 20, 30))    # Output: 60


# # Product of 4 numbers
# p = lambda a, b, c, d: a * b * c * d
# print(p(2, 3, 4, 5))    # Output: 120


#######################################################################################################
#map function 
# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))

# #create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))

# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))



# #create a new list of lengths
# colors=["red","green","blue","yellow","black"]
# print((list(map(lambda x: len(x), colors))))

# #create a new list of first characters
# print((list(map(lambda x: x[0], colors))))


# #create a new list of last characters
# print(list(map(lambda x: x[-1], colors)))


# #create a new list of reverse of each element
# print((list(map(lambda x: x[::-1], colors))))




# #Given a list 
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print((list(map(lambda x: x + 10, l))))


# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #create a new list of emails
# print((list(map(lambda i: i["email"], l))))


###############################################################################################


## filter function

# #even values
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

# #numbers greater than 50
# l=[23,67,90,12,45,52]
# print(list(filter(lambda x:x>50,l)))

# #fruitname whose length is greater than 5
# f=["apple",'orange',"grape","pineapple","grapes"]
# print(list(filter(lambda x: len(x) > 5, f)))

# #number divisible by 3 and 5
# l=[34,78,96,23,12,15]
# print(list(filter(lambda x:x%3==0 and x%5==0,l)))


##########################################################################################################
##reduce function
#sum of list , product of list
l=[1,2,3,4]
import functools
print(functools.reduce(lambda a,b:a+b,l,0))
print(functools.reduce(lambda a,b:a*b,l,1))

