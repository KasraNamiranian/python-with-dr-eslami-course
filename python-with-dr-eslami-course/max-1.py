a , b , c = input("enter 3 numbers seprating with space").split()

if float(a)>float(b):
    m1 = float(a)
else:
    m1 = float(b)

if m1 > float(c):
    print("maximum = ",m1)
else:
    print("maximum = ",float(c))