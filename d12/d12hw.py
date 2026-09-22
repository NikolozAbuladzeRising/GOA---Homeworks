name = input("შეიყვანეთ სახელი: ")

if name == "sandro":
    print("Hello admin!")
elif name == "berdia":
    print("Hello moderator!")
else:
    print("Hello user!")



num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print("პირველი რიცხვი დიდია მეორეზე")
elif num2 > num1:
    print("მეორე რიცხვი დიდია პირველზე")
else:
    print("ორივე რიცხვები ტოლია")


age = int(input("შეიყვანეთ ასაკი: "))

if age < 18:
    print("underage")
elif age == 18:
    print("teen")
else:
    print("adult")

