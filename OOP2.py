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

  def change(self):
    increment=1.5

  @classmethod
  def change(cls,amount):
    cls.increment=amount
    

harry= Employee("harry","kashyap",4000)

rohan= Employee("Rohan","Shinghaniya",4000)

print(harry.salary)
Employee.change(5)
harry.increase()
print(harry.salary)


  


