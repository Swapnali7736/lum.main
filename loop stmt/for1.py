l=[12,34,56,45,89,16,69,33]
#print even numbers
for i in l:
    if(i%2==0):
       print(i)



#Print numbers divisible by 5
for i in l:
  if(i%5==0):
     print(i)    



# Print numbers containing the digit '3'
for i in l:
  if("3" in str(i)):
     print(i)              


#sum of list
s = 0
for i in l:
    s = s + i
print(s)


#count of numbers
count = 0
for i in l:
    count = count + 1
print(count)


#count of even numbers in a list
count = 0
for i in l:
    if i % 2 == 0:
        count = count + 1
print(count)



#product of a list
l=[2,3,4,5]
p = 1
for i in l:
    p = p * i
print(p)


#print square of each number
for i in l:
    print(i **2 )



#Q.
l = [12, 4.5, 6.8, 30, "arun", "hello"]

# # Print floating point numbers

# for i in l:
#     if type(i) == float:
#         print(i)

# # Print string values

# for i in l:
#     if type(i) == str:
#         print(i)

# # Print numbers (int and float)

for i in l:
    if type(i) == int or type(i) == float:
        print(i)


#Q.
# d = {'a':23, 'b':25, 'c':28, 'd':30, 'e':22}
#print only even values

# for i in d.values():
#     if i % 2 == 0:
#         print(i)


#Q. 
# colors = ['red', 'green', 'blue', 'orange', 'black']

# # Print starting letter of each color

# for i in colors:
#     print(i[0])

# # Print last letter of each color

# for i in colors:
#     print(i[-1])

# # Print reverse of each color

# for i in colors:
#     print(i[::-1])

# # Print all colors containing letter 'b'

# for i in colors:
#     if 'b' in i:
#         print(i)



