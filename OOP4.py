class employee:
  increment=105
  no_of_employee=0
  def __init__(self,fname,lname,salary):
    self.fname=fname
    self.lname=lname
    self.salary=salary
    employee.no_of_employee+=1

  def increase(self):
    self.salary=int(self.salary * self.increment)

  @classmethod
  def change_increment(cls,amount):
    cls.increment=amount

  @classmethod
  def from_str(cls,emp_string):
    fname,lname,salary=emp_string.split("-")
    return cls(fname,lname,salary)
  

harry=employee('nisha','kashyap',4400)

nisha=employee.from_str("nisha_kashyap-jackson-760000")

rohan=employee('rohan','sharma',4400)

print(nisha.salary)

#print(harry.salary)
#employee.change_increment(4)
#harry.increase()
#print(harry.salary)



