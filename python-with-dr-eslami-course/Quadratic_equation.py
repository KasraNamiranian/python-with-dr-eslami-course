import numpy as np
a,b,c = input("enter x**2,x**1,x**0 coefficents: ").split()

a = int(a)
b = int(b)
c = int(c)

delta = pow(b,2) - 4*a*c
if delta<0:
    print("no root!!!")
elif delta == 0:
    print("root= ","{:.3f}".format(-b/(2*a)))
else:
    print("root1= " ,((-b-np.sqrt(delta)) / (2*a)) )
    print("root2= " , ((-b+np.sqrt(delta)) / (2*a)) )