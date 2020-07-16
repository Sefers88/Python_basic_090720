while True:
    list_count = input("Введите количество элементов списка: ")  # Пользователь вводит количество элементов в списке
    if list_count.isdigit():                                     # Проверим ввел пользователь число или елозил лицом
        list_count = int(list_count)
        break

    print("Ошибка ввода, введите число.")

user_list = []
i = 0
el = 0
while i < list_count:
    user_list.append(input("Введите следующее значение списка: "))  # Пользователь вводит значение элементов в списке
    i += 1

for elem in range(int(len(user_list)/2)):                  # Программа меняет местами соседние элементы, если кол-во элементов не четное, последний элемент остается на месте
        user_list[el], user_list[el + 1] = user_list [el + 1], user_list[el]
        el += 2
print(user_list)
