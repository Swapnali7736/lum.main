######  DATATYPES ######

# #numeric type - int,float,complex

# x=10 #int
# y=2.5 #float
# z=5+6j #complex


# #text type - string " "

# s="hello world"  #string
# print(s)
# print(s[0])
# print(s[4])
# print(len(s))
# print(s[0:5])
# print(s[6:11]) 
# print(s[1:5]) #1st index to 4th index
# print(s[ :5]) #default start index 0
# print(s[2: ]) #default stop index up to last of string
# print(s[::-1]) #reverse of string
# print(s[-1]) #to read last character


# #Q. Given a string s, write a Python program to:
# s = "python coding is easy and fun"
# # a) Find the length of the string.
# print(len(s))
# # b) Find the reverse of the string.
# print(s[::-1])
# # c) Print the first character.
# print(s[0])
# # d) Print the last character.
# print(s[-1])
# # e) Print the characters from the second index to the tenth character.
# print(s[2:11])
# # f) Print the 13th character.
# print(s[12])
# # g) Print the character at the fifth index.
# print(s[5])


#sequence type - list,tuple

#list[]
# l=[10,20,30,40,60]
# print(l[1])
# l[1]=50
# print(l)
# print(l[2: ])
# print(l+[80,90])
# print(l*3)
# print(len(l))
# l.append(5)
# print(l)


# #Q.  #Declare a list 5 colors
# colors=["red","blue","green","orange","pink"]

# #Add a new color 'yellow' to the list 
# colors.append("yellow")
# print(colors)

# #change the second color to black 
# colors[1]="black"

# #print the updated list 
# print(colors)

# #print the second last color 
# print(colors[-2])

# #print the number of colors 
# print(len(colors))

# #print the reverse of list
# print(colors[::-1])


# #tuple()
# t=(10,20,30)
# print(t[1])
# t[1]=50  #error because tuple is immutable ie we cannot change it after creation
# print(t)

# ###  CONCATENATION ###
# a="hello"+"world"
# print(a)

# s="12"+"12"
# print(s)

# b=12+12 #it adds because its not a string
# print(b)


# ###   REPETITION #####
# s="hello"
# print(s*2)

# a="12"
# print(a*3)

# s=12*2 #It multiplies because its not a string
# print(s)


# #set type - set{}
# s={1,2,3,4}
# print(s)
# s.add(5)
# print(s)
# s={1,2,3,3,4,2,5,4} # output should be unique here , duplicates are not allowed
# print(s)

# # # dictionary
# d={"name":"anu","age":23,"course":"python"}
# print(d)
# print(d["course"]) #used to access a value
# d["age"]=24 # used to update a dictionary
# print(d)
# d["place"]="ekm" # used to add in dictionary
# print(d)
# print(d.keys()) # used to get key 
# print(d.values())  #used to get values
# print(d.items())  #used to get key value pairs



# #Q1.  Given list ,
# l = [12, 45, 23, 67]
# #print the second element.
# print(l[1])

# #Q2. Given the nested list:
# l= [['Arun', 13], ['Amal', 24], ['Anu', 12]]

# # a) Print the second element.
# print(l[1])
# # b) Print the second name.
# print(l[1][0])


# #Q3. Given the dictionary:
# d= {
#     101: ['Arun', 23, 'EKM'],
#     102: ['Amal', 25, 'TVM']}

# # a) Print the second element.
# print(d[102])
# # b) Print the second name.
# print(d[102][0])


#Boolean type - bool
#Represents True or False

#none type - none
#x=None
