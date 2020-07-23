import random

numbers_list = [random.randint (1,300) for i in range (12)] #Задаем список заполненный 12 рандомными числами от 1 до 300
print (f'{numbers_list}')

result_list = [el for num, el in enumerate(numbers_list) if numbers_list[num-1] < numbers_list[num]] #Создаем новый список и вводим условия для решения задачи
print (f'Новый список по условиям задания: {result_list}')
