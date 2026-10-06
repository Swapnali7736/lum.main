##new list for square of each elements of the given list
# l=[1,2,3,4]
# new_list=[i**2 for i in l]
# print(new_list)

##add 5 in the list
# new=[5 for i in l]
# print(new)


#Given a list l=[12,45,34,67,90]
# create a new list with even values 

# l=[12,45,34,67,90]
# new_list=[i for i in l if i%2==0]
# print(new_list)

#create a new list with values greater than 50

# new_list=[i for i in l if i>50]
# print(new_list)


#Given  a list colors=['red','green','blue','orange']
# create a new list with first letter of each color

# colors=["red","green","blue","orange"]
# new_list=[i[0] for i in colors]
# print(new_list)

# create a new list with length of each color

# new_list=[len(i) for i in colors]
# print(new_list)


# #create a new list with square root of each element
# l=[25,16,9,36]
# new_list=[i**0.5 for i in l]
# print(new_list)


# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new_list= [ i for i in d]
# print(new_list)

# # # create a list of marks
# new_list= [ i for i in d.values()]
# print(new_list)


# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# # #create a list of string values
# new_list=[i for i in l if type(i)==str]
# print(new_list)

# # #create a list of floats
# new_list=[i for i in l if type(i)==float]
# print(new_list)

# # #create a list of positive numbers
# new_list=[i for i in l if (type(i)==int or type(i)==float) and i>0]
# print(new_list)



# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# new_list=[i for i in fruits if len(i)>6]
# print(new_list)

# # #create a new list with elements whose value is divisible by 3 in range(1,101)
# new_list=[i for i in range(1,101) if i%3==0]
# print(new_list)


# # Given 
# s="python coding  is easy and fun"
# # # create a new list with only vowels
# new_list=[i for i in s if i in "aeiouAEIOU"]
# print(new_list)


###################################################################################################
##   SET COMPREHENSION


## Create a set of all characters in a string except spaces using set comprehension.
s="python coding is easy and fun"
new={i for i in s if i!=" "}
print(new)


##Create a set of all vowels present in a string using set comprehension.
# # new={i for i in s if i in "aeiouAEIOU"}
# # print(new)

# print(s.split())
# print(s.split("i"))


# print(s.split("a"))




#############################################################################################################
#     DICTIONARY COMPREHENSION

# #new dict for square of each elements of list
# l=[10,20,30,40]
# new={i:i**2 for i in l}
# print(new)


# l=[10,20,30,40]
# #new dict where keys are index of each number and values are numbers from not list
# new = {i: l[i] for i in range(0,len(l))}
# print(new)




# #s="python coding  is easy and fun"
# #new dict where keys are words and values are length of each word
# s = "python coding is easy and fun"
# new = {i: len(i) for i in s.split()}
# print(new)



