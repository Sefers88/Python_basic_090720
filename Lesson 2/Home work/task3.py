while True:
    month = input("Введите текущий месяц цифрами: ")       # Пользователь вводит текущий месяц
    if month.isdigit():                                    # Проверем ввел пользователь число или совершил ошибку при вводе
        month = int(month)
        break

    print("Ошибка ввода.")

seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']


if month == 1 or month == 12 or month == 2:       # проверяем и выводим на экран какому времени года в словаре и списке соответствует введеный месяц
    print(seasons_dict.get(1))
    print(seasons_list[0])

elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])

elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])

else:
    print("Такого месяца не существует")    # Если пользователь ввел число, но ошибся с вводом месяца появляется сообщение об ошибке
