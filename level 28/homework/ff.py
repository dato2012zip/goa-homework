
list1 = [2, 51, 11, 13, 51, 100]


positive_index_elements = [list1[i] for i in range(len(list1))]
print("დადებითი ინდექსების ელემენტები:", positive_index_elements)


negative_index_elements = [list1[i] for i in range(-1, -len(list1)-1, -1)]
print("უარყოფითი ინდექსების ელემენტები:", negative_index_elements)


list1[-1] = 999
print("ბოლო ელემენტის შეცვლის შემდეგ:", list1)


list1[4] = 77
print("მე-5 ელემენტის შეცვლის შემდეგ:", list1)


list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


print("10 ელემენტიანი სია:", list2)

first_three = list1[:3]
last_three = list1[-3:]
middle_four = list1[1:5]
print("პირველი სამი:", first_three)
print("ბოლო სამი:", last_three)
print("შუა 4 დადებითი ინდექსით:", middle_four)


first_three_neg = list1[-len(list1):-len(list1)+3]
last_three_neg = list1[-3:]

print("პირველი სამი (:", first_three_neg)
print("ბოლო სამი :", last_three_neg)




text = "Hello"
reversed_text = text[::-1]
print("შეტრიალებული სტრინგი:", reversed_text)
