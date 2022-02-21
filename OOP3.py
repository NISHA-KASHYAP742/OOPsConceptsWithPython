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
  

harry=employee('nisha','kashyap',4400)

rohan=employee('rohan','sharma',4400)

print(harry.salary)
employee.change_increment(4)
harry.increase()
print(harry.salary)



