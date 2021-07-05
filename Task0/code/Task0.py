import random


list = []
list_2 = []
maximum = float('-inf')
maximum_index = 0

for i in range(30):
     list.append(int(random.uniform(-100, 100)))

for i in range(len(list)):
    if list[i] > maximum:
        maximum = list[i]
        maximum_index = i
    if list[i]%2 !=0:
       list_2.append(list[i])
print("Сгенерований список: ", list," . \n")
print("Максимальний элемент списка: ",maximum ,". \n",
           "Індекс максимального елемента: ",maximum_index,". \n"  )
if len(list_2) != 0:
   print("Cписок непарних чисел : \n")
   list_2.sort(reverse= True)
   print(list_2)
   print("\n")
else:
   print("Непарних чисел не виявлено")
   
print("Пари чисел:")
for i in range(len(list)):
    if list[i] < 0 and i!=0:
        if list[i-1] < 0:
           flag = True
           print(list[i-1],"  ",list[i])

if flag != True:
   print("Пар відємних чисел не виявлено.")
