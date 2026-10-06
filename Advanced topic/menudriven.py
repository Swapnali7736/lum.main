def file_read():
    file_name=input("enter filename:")
    f=open(file_name,"r")
    content=f.read()
    print(content)

def file_write():
    file_name=input("enter filename:")
    s=input("enter the content")
    f=open(file_name,"w")
    content=f.write(s)
    print(content)

def file_append():
    file_name=input("enter filename:")
    b=input("enter the content")
    f=open(file_name,"a")
    content=f.write(b)
    print(content)

def file_search():
    file_name=input("enter filename:")
    c=input("enter the word")
    f=open(file_name,"r")
    content=f.read()
    if c in content:
            print("found")
    else:
            print("not found") 

def file_delete():
    file_name=input("enter filename:")
    import os
    os.remove(file_name)   


while(1):
    print("menu driven file operations")
    print("1.file read")
    print("2.file write")
    print("3.file append")
    print("4.file search")
    print("5.file delete")
    print("6.exit")

    ch=int(input("enter your choice:"))

    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        exit()