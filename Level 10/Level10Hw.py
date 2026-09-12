password = "SecretWord"
guess = input()
while guess != password:
    guess = input()
print("ACCESS GRANTED")

# როგორ მუშაობს კოდი:
# password = "SecretWord": ადგენს სწორ პაროლს რომელიც არის "SecretWord"
#    guess = input() ელოდება მომხმარებლის გამოცნობას
# while guess!= password: სანამ გამოიცნობს ცდილობს რომ ცადოს ძალიან სარისკო ცდა
# print("ACCESS GRANTED") აქ პრინტი გამოიტანს ტერმინალში სწორე პაროლი ანუ სწორედ გამოცნობილი და შესვლაც შესაძლებელია სისტემაში