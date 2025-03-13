
i = 1
while i <= 5:
    print(i)
    i += 1


i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("ჯამი 1-დან 10-მდე:", sum)



num = int(input("შეიყვანეთ რიცხვი:"))
i = 1
while i <= num:
    print(i)
    i += 1


correct_password = "1234"
user_input = input("შეიყვანეთ პაროლი:")

while user_input != correct_password:
    print("პაროლი არასწორია სცადეთ კიდევ.")
    user_input = input("შეიყვანეთ პაროლი:")

print("პაროლი სწორია!")


correct_number = 7
guess = int(input("გამოიცანით რიცხვი:"))

while guess != correct_number:
    print("არასწორი რიცხვი! სცადეთ ისევ.")
    guess = int(input("გამოიცანით რიცხვი:"))

print("თქვენ გამოიცანით სწორი რიცხვი")



