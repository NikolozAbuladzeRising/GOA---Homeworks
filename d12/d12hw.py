name = input("შეიყვანეთ სახელი: ")

if name == "sandro":
    print("Hello admin!")
elif name == "berdia":
    print("Hello moderator!")
else:
    print("Hello user!")



first = float(input("შეიყვანეთ პირველი რიცხვი: "))
second = float(input("შეიყვანეთ მეორე რიცხვი: "))

if first > second:
  print("first number is greater then second")
elif second > first:
  print("second number is greater then first")
else:
  print("both numbers are equal")




age = 18

if age < 18:
    print("underage")
elif age == 18:
    print("teen")
else:
    print("adult")

