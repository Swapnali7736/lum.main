import sqlite3
con=sqlite3.connect("company.db")
command="""create table if not exists employee(empid int primary key,name varchar(30),age int,place varchar(30),gender varchar(10),designation varchar(30),salary int)"""
#primary key field used to identify a particular record
#It must be unique/no duplicate value
con.execute(command)
# print("Table created")


# #INSERT OPERATION
# command="""insert into employee(empid,name,age,place,gender,designation,salary)
#         values(101,"anu",23,"knlr","female","developer",240000),
#         (102,"amol",26,"ekm","male","devops",260000),
#         (103,"anika",22,"tvm","female","ai engineer",280000),
#         (104,"aswin",25,"klm","male","te""ster",290000),(105,"neha",29,"mlr","female","tester",39000)"""
# con.execute(command)
# con.commit()
# print("Data Inserted Successfully")


# #READ OPERATION
# # command="select * from employee"
# # To read all employee records with all the attributes
# e=con.execute("select * from employee")
# print(e.fetchall())


##all employee records with attributes name,age
# e=con.execute("select name,age from employee")
# print(e.fetchall())

##employee records with empid=101(return all attributes)
# e=con.execute("select * from employee where empid=101")
# print(e.fetchall())

##employee records with empid=101(specific attributes name,age)
# e=con.execute("select name,age from employee where empid=101")
# print(e.fetchall())

# ##read all employee records having age>=25 and salary<3000
# e=con.execute("select * from employee where age>=25 and salary<30000")
# print(e.fetchall())


# ##read all employee records with empid other than 102
# e=con.execute("select * from employee where (empid!= 102)")
# print(e.fetchall())

# ##read all employee records having places="ekm" or age<=25
# e=con.execute("select * from employee where place='ekm' or age<=25")
# print(e.fetchall())

##between
# ##employee records having salary between 20000 and 30000 
# e=con.execute("select * from employee where salary between 20000 and 30000")
# print(e.fetchall())


# ## employee records having age  between 20 and 25(return name,age)
# e=con.execute("select name,age from employee where age between 20 and 25")
# print(e.fetchall())

##like
# #pattern matching
# % - 0 or more characters
# _ - exactly one character

# #employee record having name starting with "A"
# e=con.execute("select name,age from employee where name like 'A'")
# print(e.fetchall())

# #employee record having 3 letter name starting with "A"
# e=con.execute("select * from employee where name like 'A__'")
# print(e.fetchall())

# #employee record with place starting with "E"
# e=con.execute("select * from employee where name like 'E__'")
# print(e.fetchall())

# #employee record having 3 letter placename ending with letter "m"
# e=con.execute("select * from employee where place like '__m'")
# print(e.fetchall())

#employee record having age<25 and name starting with letter "A"
# e=con.execute("select * from employee where age<25 and name like 'A%'")
# print(e.fetchall())

# #employee record having salary=50000 and 3 letter placements starting with "T"
# e=con.execute("select * from employee where salary=50000 and name like 'T__'")
# print(e.fetchall())


#in
# #employee records having age=30 or age=25
# e=con.execute("select * from employee where age in(25,30)")
# print(e.fetchall())

# ##order by
# #order by ascending
# e=con.execute("select * from employee order by name")
# print(e.fetchall())

# #descending order by name
# e=con.execute("select * from employee order by name desc")
# print(e.fetchall())

# #descending order by age
# e=con.execute("select * from employee order by age desc")
# print(e.fetchall())

# ##distinct
# e=con.execute("select distinct (place) from employee")
# print(e.fetchall())


# ##UPDATE OPERATION
# con.execute('update employee set name="Kiran" ,age=28 where empid=102')
# con.commit()
# print("updated successfully")

##DELETE  OPERATION
con.execute('delete from employee where empid=103')
con.commit()
print("deleted successfully")



