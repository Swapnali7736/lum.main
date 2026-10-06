# NUMBER BUILT-IN FUNCTIONS

print("Absolute:", abs(100))
print("Absolute:", abs(-100))

print("Power:", pow(5, 3))

print("Maximum:", max(10, 20, 30))
print("Minimum:", min(10, 20, 30))

print("Sum:", sum([10, 20, 30]))

print("Divmod:", divmod(10, 3))

print("Round:", round(3.456, 2))


# MATH MODULE FUNCTIONS

import math

print("Square Root:", math.sqrt(81))

print("Factorial:", math.factorial(5))

print("Integer Square Root:", math.isqrt(17))

print("Floor:", math.floor(3.8))

print("Ceil:", math.ceil(3.2))

print("LCM:", math.lcm(12, 18))

print("GCD:", math.gcd(12, 18))


# RANDOM MODULE FUNCTIONS

import random

print("Random:", random.random())

print("Random Integer:", random.randint(1,10))

print("Random:", random.randrange(100,999,2))

print("Random Choice:", random.choice(2,4,6,8,12))


# STRING FUNCTIONS

s = "Python Coding 123"

print("String:", str(123))

print("Length:", len(s))

print("Type:", type(s))

print("Capitalize:", s.capitalize())

print("Upper:", s.upper())

print("Lower:", s.lower())

print("Index:", s.index("C"))

print("Find:", s.find("Coding"))

print("Count:", s.count("o"))

print("Replace:", s.replace("Python","Java"))

print("Strip:", "  hello  ".strip())

words = ["Python","Coding"]
print("Join:", "-".join(words))

print("Is Digit:", "123".isdigit())

print("Is Alpha:", "Python".isalpha())

print("Is Alnum:", "Python123".isalnum())

print("Is Space:", "   ".isspace())

print("Is Upper:", "PYTHON".isupper())

print("Is Lower:", "python".islower())

print("Starts With:", s.startswith("Python"))

print("Ends With:", s.endswith("123"))


# LIST FUNCTIONS

l = [10,20,30,40]

print("List:", list(l))

print("Length:", len(l))

print("Type:", type(l))

l.append(50)
print("Append:", l)

l.insert(1,15)
print("Insert:", l)

l.extend([60,70])
print("Extend:", l)

print("Index:", l.index(30))

print("Count:", l.count(20))

print("Pop:", l.pop())

l.pop(1)
print("Pop Index:", l)

l.remove(30)
print("Remove Element:", l)

l.clear()
print("Clear:", l)


l1 = [5,3,1,4]

l2 = l1.copy()
print("Copy:", l2)

l1.reverse()
print("Reverse:", l1)

l1.sort()
print("Sort:", l1)


# SET FUNCTIONS

s = {10,20,30}

print("Set:", set([1,2,3]))

print("Length:", len(s))

print("Type:", type(s))

s.add(40)
print("Add:", s)

s.update([50,60])
print("Update:", s)

s.remove(20)
print("Remove:", s)

s.discard(100)
print("Discard:", s)

print("Pop:", s.pop())

a = {1,2,3}
b = {3,4,5}

print("Union:", a.union(b))

print("Intersection:", a.intersection(b))

print("Difference:", a.difference(b))

print("Symmetric Difference:", a.symmetric_difference(b))



# DICTIONARY FUNCTIONS

d = {"name":"Anu","age":23,"place":"Kochi"}

print("Dictionary:", dict(name="Anu", age=23))

print("Length:", len(d))

print("Type:", type(d))

print("Keys:", d.keys())

print("Values:", d.values())

print("Items:", d.items())

print("Get:", d.get("name"))

print("Pop:", d.pop("age"))

print("Pop Item:", d.popitem())

d.update({"course":"Python"})
print("Update:", d)

d2 = d.copy()
print("Copy:", d2)

d.clear()
print("Clear:", d)