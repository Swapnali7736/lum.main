import mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")

# # connection to the db server

# c=con.cursor()  # to execute sql commands 

# c.execute("create database mydb2")
#                                 #    no need to give .db extension
# print("database created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="mydb2")
#connection to the mydb2 file
c=con.cursor()
# c.execute('''create table if not exists employee(empid int primary key,name varchar(20),age int,salary int,gender varchar(20),place varchar(20))''')
# print("Table created")

# c.execute('''insert into employee(empid,name,age,salary,gender,place)values(101,"Anu",21,23000,"M","tvm"),
#             (102,"Bina",22,25000,"F","ktm"),(103,"cima",23,28000,"F","ekm"),(104,"diya",26,49000,"F","tirur"),
#             (105,"elza",29,78000,"F","Aluva")''')
# con.commit()
# print("Data inserted successfully")


# #Read operation
# c.execute('select * from employee')
# k=c.fetchall()
# print(k)

# # To read particular record
# c.execute('select * from employee where empid=102')
# k=c.fetchall()
# print(k)

# #Read all records with attributes name,age
# c.execute('select name,age from employee where empid=101')
# k=c.fetchall()
# print(k)

# ##read all employee records having age>=25 and salary<3000
# c.execute("select * from employee where age>=25 and salary<30000")
# k=c.fetchall()
# print(k)


# ##read all employee records with empid other than 102
# c.execute("select * from employee where (empid!= 102)")
# k=c.fetchall()
# print(k)

# ##read all employee records having places="ekm" or age<=25
# c.execute("select * from employee where place='ekm' or age<=25")
# k=c.fetchall()
# print(k)

##between
# ##employee records having salary between 20000 and 30000 
# c.execute("select * from employee where salary between 20000 and 30000")
# k=c.fetchall()
# print(k)


# ## employee records having age  between 20 and 25(return name,age)
# c.execute("select name,age from employee where age between 20 and 25")
# k=c.fetchall()
# print(k)


##like
# #pattern matching
# % - 0 or more characters
# _ - exactly one character

# #employee record having name starting with "A"
# c.execute("select name,age from employee where name like 'A'")
# k=c.fetchall()
# print(k)

# #employee record having 3 letter name starting with "A"
# c.execute("select * from employee where name like 'A__'")
# k=c.fetchall()
# print(k)


# #employee record having 3 letter placename ending with letter "m"
# c.execute("select * from employee where place like '__m'")
# k=c.fetchall()
# print(k)

# # employee record having age<25 and name starting with letter "A"
# c.execute("select * from employee where age<25 and name like 'A%'")
# k=c.fetchall()
# print(k)

# #employee record having salary=50000 and 3 letter placements starting with "T"
# c.execute("select * from employee where salary=50000 and name like 'T__'")
# k=c.fetchall()
# print(k)


#in
# #employee records having age=30 or age=25
# c.execute("select * from employee where age in(25,30)")
# k=c.fetchall()
# print(k)

##order by
# #order by ascending
# c.execute("select * from employee order by name")
# k=c.fetchall()
# print(k)

# #descending order by name
# c.execute("select * from employee order by name desc")
# k=c.fetchall()
# print(k)

# #descending order by age
# c.execute("select * from employee order by age desc")
# k=c.fetchall()
# print(k)

# # ##distinct
# c.execute("select distinct (place) from employee")
# k=c.fetchall()
# print(k)


# ##UPDATE OPERATION
# c.execute('update employee set name="Kiran" ,age=28 where empid=102')
# con.commit()
# print("updated successfully")

# ##DELETE  OPERATION
# c.execute('delete from employee where empid=103')
# con.commit()
# print("deleted successfully")




