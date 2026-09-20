
age = 20

if age < 18:
    print("underage")
elif age == 18:
    print("teen")
else:
    print("adult")



for i in range(3):
    number = int(input("შეიყვანე რიცხვი: "))
    
    if number == 0:
        print("zero")
    elif number > 0:
        print("positive")
    else:
        print("negative")
