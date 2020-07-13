user_number = int(input('Введите число в котором вы хотите найти наибольшую цифру: '))
max_number = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
max_number = str(max_number)
print('Самая большая цифра в введонном числе ' + max_number)