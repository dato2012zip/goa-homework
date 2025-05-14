# Sliceing გამოიყენება სტრინგიდან, სიიდან ან სხვა ინდექსირებადი ობიექტიდან მის ნაწილობრივ ამოსაღებად.
# Syntax არის: ობიექტიstart:stop:step
# სადაც:
#  start: საწყისი ინდექსი მოსათვლელი პოზიცია
#  stop: სად უნდა გაჩერდეს stop ინდექსი უკვე აღარ შედის შედეგში
#  step  რამდენით უნდა გაზარდოს ინდექსი ყოველ ნაბიჯზე

surname = input("შეიყვანე შენი გვარი: ")

if surname.endswith("shvili"):
    print("Hello")
elif surname.endswith("dze"):
    print("Bye")



sentence = input("შეიყვანე წინადადება: ")
index = int(input("შეიყვანე ინდექსი: "))

print(sentence[0:index])  





