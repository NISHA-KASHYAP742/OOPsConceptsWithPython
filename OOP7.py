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

    def __add__(self,other):
      return self.salary + other.salary

    def __repr__(self):
      return 'employee({},{},{}'.format(self.fname,self.lname,self.salary)

    def __str__(self):
      return 'the name is{}'.format(self.fname)


harry=employee('nisha','kashyap',201333)
rohan=employee("akshay","kumar",12000)
  
#print('85'+'125')
#a=6
#print(a.__add__(7))
#print(a.__mul__(7))
#print(str(harry))
print(harry)





