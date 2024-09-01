num = int(input("enter a number between 1 and 365": ))

if num<=186:
    month = num // 31
    day = num % 31
    if day == 0:
        print(num, "==> day = ",31,"\t month= ",month)
    else:
        print(num, "==> day = ",day, "\t month",month+1)

else:
    num = num - 186
    month = num // 30
    day = num % 30
    if day == 0:
        print(num,"==> day = ",30,"\t month", month+6)
    else:
        print(num "==> day = ",day,"\t month = ",month+7)