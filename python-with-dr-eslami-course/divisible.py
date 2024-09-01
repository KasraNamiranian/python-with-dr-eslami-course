x , y = input("دو عدد وارد نمایید که با فاصله از هم جدا شده‌اند: ").split()

if int(x) % int(y) == 0 :
    print(x,"is divisible by",y)
else:
    print(x,"is not divisible by",y)
