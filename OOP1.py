class Employee:
  
  increment = 2
  no_of_employee = 0
  def __init__(self,name,lname,salary):
    self.name=name
    self.lname=lname
    self.salary=salary
    Employee.no_of_employee +=1
    
  def increase(self):
    self.salary = int(self.salary*Employee.increment)
    
print(Employee.no_of_employee) 
harry= Employee("harry","kashyap",44000)
rohan= Employee("Rohan","Shinghaniya",4000)
print(Employee.no_of_employee)

print("*******************************************************88")
#this can also be used.
#harry.name="A"
#harry.lname="d"
#harry.salary="5K"

#rohan.name="Rohan"
#rohan.lname="Shinghaniya"
#rohan.salary="5K"

#print(rohan.__dict__)
#rohan.increment = 9
#print(rohan.__dict__)

#print(rohan.salary)




#print(rohan.name)



