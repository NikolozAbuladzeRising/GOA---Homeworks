password = "sandro123"
user_input = ""

while user_input != password:
    user_input = input("შეიყვანეთ პაროლი: ")


print("access granted!")



total_sum = 0
number = 20

while number >= 1:
    total_sum += number
    number -= 1

print(total_sum)



num1 = int(input())
num2 = int(input())

total_sum = 0
current = num1

while current >= num2:
    total_sum += current
    current -= 1

print(total_sum)




num1 = int(input())
num2 = int(input())

total_sum = 0
current = num2

while current <= num1:
    total_sum += current
    current += 1

print(total_sum)


secret_num = 7
user_guess = 0

while user_guess != secret_num:
    user_guess = int(input())

print("You guessed it!")


