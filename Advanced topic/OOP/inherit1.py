#multiple inheritance
#parent
#hospital-hname,location,showdetails()
#department-dname,doctorname,showdepartmentdetails()
#child
#patient-pid,pname,pgender,pplace,padmdate,pdisdate,fullsummary(),dischargedetails()

# class Hospital:
#     def __init__(self):
#         self.hname=input("enter the hname:")
#         self.location=input("enter the location:")
#     def showdetails(self):
#         print(self.hname,self.location)

# class Department:
#     def __init__(self):
#         self.dname=input("enter the dname:") 
#         self.docname=input("enter the docname:")
#     def showdepartmentdetails(self):
#         print(self.dname,self.docname) 

# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.pid=int(input("enter the pid:"))
#         self.pname=input("enter the pname:")
#         self.pgender=input("enter the pgender:")
#         self.pplace=input("enter the pplace:")
#         self.padmdate=input("enter the admdate:")
#         self.pdisdate=input("enter the disdate:")

#     def fullsummary(self):
#         # Hospital.showdetails(self)
#         # Department.showdepartmentdetails(self)
#         print("Hospital:", self.hname,"Location:", self.location,"Department:", self.dname,"Doctor:", 
#               self.docname,"Patient ID:", self.pid,"Patient Name:", self.pname,"Gender:", self.pgender,
#               "Place:", self.pplace,"Admission Date:", self.padmdate)

#     def dischargedetails(self):
#         print("Patient Name:", self.pname,"Discharge Date:", self.pdisdate)


# p = Patient()
# p.fullsummary()
# p.dischargedetails()                 















# hospital-name,location,showdetails()   parent class
# departmnt-name,docname,showdepdetails() parent class
# patient-id,name,gender,place,admdate,dischargedate,fullsammary(),dischargedeails() child class

class hospital:
    def __init__(self):
        self.hname=input("enter the hospital name:")
        self.hloc=input("enter the location:")

    def showdetails(self):
        print("hospital name:",self.hname)
        print("hospital location:",self.hloc)

class department:
    def __init__(self):
        self .dname=input("enter the department name:")
        self.docname=input("enter the docter name:")

    def showdepdetails(self):
        print("department name:",self.dname)
        print("docter name:",self.docname)

class patient(hospital,department):
    def __init__(self):
        hospital.__init__(self)
        department.__init__(self)
        self.id=input("enter the patient id:")
        self.pname=input("enter the patient name:")
        self.gender=input("enter the patient gender:")
        self.place=input("enter the patient place:")
        self.admdate=(input("enter the admission date:"))
        self.disdate=" "
        print()

    def setdiscahrgedetails(self):
        self.disdate=input("enter the discharge details: ")

    def fullsummary(self):
        hospital.showdetails(self)
        department.showdepdetails(self)
        print("patient id:",self.id,)
        print("patient name:",self.pname)
        print("gender:",self.gender)
        print("place: ",self.place)
        print("admission date:",self.admdate)
        if self.disdate==" ":
            print("not yet discharge")
        else:
            print("discharge date:",self.disdate)
        print()
    def discharge(self):
        print("admission date:",self.admdate)
        print("discharge date:",self.disdate)
        print("docter:",self.docname)


p=patient()
p.fullsummary()
p.setdiscahrgedetails()
p.fullsummary()