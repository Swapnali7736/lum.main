# #1write a program to read a text file and displays the number of lines in a file

# f=open("k.txt","r")
# # content=f.readlines()
# # print(len(content))
# f.close()

# #write a program to display the number of words in a file 

# f=open("k.txt","r")
# # content=f.read()
# # c=content.split()
# # print(len(c))
# f.close()


# #write a program to update the second line in a file 

# f=open("k.txt","r")
# # content=f.readlines()
# # content[1]="helloooo"
# # f.close()
# # f=open("k.txt","w")
# # f.writelines(content)
# # print(content)
# f.close()   

# #write a program to display the last 5 lines in a file 

# f=open("k.txt","r")
# # content=f.readlines()
# # print(content[-5:])
# f.close()

# #program to search a particular word in a file 

# f=open("k.txt","r")
# # a=input("enter a word")
# # content=f.read()
# # if a in content:
# #         print("word found")
# # else:
# #         print("not found")    
# f.close()

# #find the number of letters,digits,and spaces in a file

# f=open("k.txt","r")
# l=0
# d=0
# s=0
# content=f.read()
# for i in content:
#     if i.isalpha():
#         l=l+1
#     elif i.isdigit():
#         d=d+1
#     elif i.isspace():
#         s=s+1
#     else:
#         pass    
# print(l)              
# print(d)              
# print(s)              
# f.close()


#reverse the lines in a file
 
f=open("k.txt","r")
content=f.readlines()
rev=(content[::-1])
f=open("k.txt","w")
f.writelines(rev)
f.close()