def permutation(a, value):       # Создаем условие при котором введенное пользователем число встанет по порядку
    max_value = max(a)
    if value > max_value:
        a.insert(0, value)
    elif value in a:
        a.insert(-a[::-1].index(value),value)
    else:
        a.apend(value)

my_list = [7, 5, 3, 3, 2]   # Создаем список и вводим свои цифры
print(my_list)

first_number = int(input("Введите число для добавления в список: "))  # Предлагаем пользователю ввести 1 доп число
permutation(my_list,first_number)  # Введенное число попадает в список и принимает свой числовой порядок
print(my_list)

second_number = int(input("Введите число для добавления в список: "))  # Предлагаем пользователю ввести 2 доп число
permutation(my_list,second_number)   # Введенное число попадает в список и принимает свой числовой порядок
print(my_list)




