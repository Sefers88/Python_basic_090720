with open('task3.txt', 'r', encoding='utf-8') as user_file:
    sal = []  # Список для расчета средннй величины оклада всех сотрудников
    bad_pay = [] # Список для сотрудников с окладом меньше 20 000
    user_list = user_file.read().split('\n')
    for i in user_list:  # Сортировка сотрудников по окладу < 20000
        i = i.split()
        if int(i[1]) < 20000:
           bad_pay.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000: {bad_pay}, средний оклад: {sum(map(int, sal)) / len(sal)}')
