class Demo:
    a=0
    b=0
Ob = Demo
print("Original Values = ", "a= ", Ob.a, "b = ",Ob.b)
Demo.a = 1
Demo.b = 2
print("Manipulated Values = ", "a= ", Ob.a, "b = ",Ob.b)

