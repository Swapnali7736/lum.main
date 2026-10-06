f=open("marks.txt","w")
a=["anu 80\n","rahul 65\n","meera 90\n","arun 70\n"]
f.writelines(a)


f=open("marks.txt","r")
s=f.readlines()
print(s)
f=open("names.txt","w")

for i in s:
    l=i.split()
    if(int(l[1]) > 75):
        f.writelines(l[0] + "\n")

