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
  @staticmethod
  def isopen(day):
    if day=="sunday":
      return False
    else:
      return True
class programmer(employee):

  def __init__(self,fname,lname,salary,proglang,exp):
    super().__init__ (fname,lname,salary)
    self.prolang=proglang
    self.exp=exp


  def increase(self):
    self.salary=int(self.salary * (self.increment+0.5))
    return self.salary



nisha=programmer('nisha','kashyap',456000,'python','4years')
print(nisha.salary)
#print(help(programmer))
  


