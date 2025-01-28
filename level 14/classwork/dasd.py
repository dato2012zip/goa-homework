age = int(input("შეიყვანეთ თქვენი ასაკი: "))
has_driver_license = input("გქონდეთ მართვის მოწმობა (დიახ/არა): ").lower()

if age >= 18 and has_driver_license == "დიახ":
    print("თქვენ შეგიძლიათ შეხვალთ ქვეყანაში.")

    print("თქვენ არ გაქვთ უფლება შესვლის.")
