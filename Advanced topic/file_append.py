# f=open("ab.txt","a")
# f.write("python")
# f.close()



#write a python program to read contents from one text file and appends it into another text file

f=open("k.txt","r")
a=f.read()
f.close()

f=open("ab.txt","a")
f.write(a)
f.close()





# f=open("k.txt","a+")
# a=f.read()
# f.write(a)




#seek and tell
f=open("ab.txt","a+")
print("current position",f.tell())
f.write("python")
print("current position",f.tell())

f.seek(0)
print("current position",f.tell())
content=f.read()
# print("content",content)