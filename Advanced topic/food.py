f=open("swiggy.txt","w")
a=["burger\n","pizza\n","fries\n","rice\n"]
f.writelines(a)

f=open("zomato.txt","w")
b=["burger\n","pizza\n","fries\n","idli\n","cake\n","dosa\n"]
f.writelines(b)



f=open("swiggy.txt","r")
s=f.readlines()
f=open("zomato.txt","r")
z=f.readlines()

k=s+z
d={}
for i in k:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)    