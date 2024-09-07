grade = int(input("Enter your score between 0-100: "))
if grade > 100:
    print("The score is out of range!")
elif grade>=90:
    print("grade A")
elif grade>=80:
    print("grade B")
elif grade>=70:
    print("grade C")
elif grade>=60:
    print("grade D")
elif grade>=0:
    print("grade F")
else:
    print("The score is out of range!")