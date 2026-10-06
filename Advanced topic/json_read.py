import json
# f=open("sample.json","r")
# content=json.load(f)
# print(content)


data=[
    {"name":"arun","age":20},
    {"name":"amal","age":23}
]
f=open("data.json","w")
json.dump(data,f)