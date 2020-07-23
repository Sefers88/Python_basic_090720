from itertools import (islice,
                       count,
                       cycle
                      )

for el in islice(count(int(input('Введите первое число с которого начать генерацию: '))), 10): #Задаем цифру отсчета и задаем генерацию следующих 10 цифра
    print(el)

print()

count = 1                          # Задаем счетчик
user_list = ['Хорошо', 44, 0.99]   # Задаем список
for el in cycle(user_list):        # Задаем условие что пока счетчик не дорстиг указанных значений из списка пичатается по 1 значени по циклу
    if count > 12:                 # Количество циклов вывода информации 12
        break
    print (el)
    count +=1
