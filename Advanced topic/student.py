f=open("total_students.txt","w")
content=["ram\n","sam\n","arun\n","anu\n","sunu\n","viha\n"]
f.writelines(content)

f=open("passed_students.txt","w")
a=["ram\n","sam\n","arun\n"]
f.writelines(a)


f=open("total_students.txt","r")
total = f.readlines()


f=open("passed_students.txt","r")
passed = f.readlines()


f=open("failed_students.txt","w")

for i in total:
    if i not in passed:
        print(i)
        f.writelines(i)




