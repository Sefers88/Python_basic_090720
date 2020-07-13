"""
исполнение не очень, по хорошему надо было ввести условие проверки ввел ли пользователь цифру от 1 до 9,
если введено число или буквы которые не соответстуют задаче запросить данные заново, опыта в программировании нет,
поэтому пока так)
"""
user_number = input("Введите цифру от 1 до 9: ")
user_number_sum1 = user_number + user_number
user_number_sum2 = user_number + user_number + user_number

user_number = int(user_number)
user_number_sum1 = int(user_number_sum1)
user_number_sum2 = int(user_number_sum2)

sum = user_number + user_number_sum1 + user_number_sum2
print (sum)