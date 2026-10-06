# Given a list
colors = ['red', 'green', 'blue', 'yellow', 'black', 'orange']

# Print each color

for i in colors:
    print(i)

# Print the first color starting with 'b'

for i in colors:
    if i[0] == 'b':
        print(i)
        break

# Print all colors except colors starting with 'b'

for i in colors:
    if i[0] != 'b':
        print(i)

# Print the first color containing letter 'n'

for i in colors:
    if 'n' in i:
        print(i)
        break

# Print all colors except colors containing letter 'n'

for i in colors:
    if 'n' not in i:
        print(i)


#Given a list l=[1,2,3,4]
# create a new list with squares of each elements

l = [1, 2, 3, 4]
new = []
for i in l:
    new.append(i**2)
print(new)

#Given a list l=[12,67,59,23]
#create a list with elements whose value is greater than 50.

l = [12, 67, 59, 23]
new = []
for i in l:
    if i > 50:
        new.append(i)
print(new)

# create a new set with elements whose value is greater than 50
l = [12, 67, 59, 23]
s = set()
for i in l:
    if i > 50:
        s.add(i)
print(s)

#Given a list l=[1,2,3,4]
#create a new dictionary where keys are numbers and values are squares of each number
l = [1, 2, 3, 4]
d = {}
for i in l:
    d[i] = i**2
print(d)

        
        