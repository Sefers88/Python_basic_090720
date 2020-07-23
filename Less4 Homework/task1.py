def worker_salary():
    try:
        work_hours = float(input('Введите количество отработанных часов работником: '))
        bid_per_hour = float(input('Введите сумму оплаты труда за 1 час: '))
        bonus = float(input('Введите размер премии сотрудника: '))
        payment = work_hours * bid_per_hour + bonus
        print(f'Размер заработной платы работника составил: {payment}')
    except ValueError:
        return print ('Ошибка при вводе чисел')

print ('Программа расчета заработной платы работника, дробные числа вводить строго через знак "."')
worker_salary()
