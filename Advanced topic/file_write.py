#write operation

# f=open(filename,accessmode)
f=open("k.txt","w") #if file already exists,then it will erase the conntents and returns its reference to f
#else it will create an empty text file and returns its reference to f

##2 methods
##   1
# f.write(string)
# f.write("hello")


##  2
# f.writelines(list)
content=["python\n","java\n","php\n"]
f.writelines(content)
f.close()