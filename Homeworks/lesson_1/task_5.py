income = int(input('Введите доходы фирмы за год: '))
cost = int(input('Введите расходы фирмы за год: '))

profit = income - cost
if profit < 0:
    print ('Фирма работает в убыток, сумма убытка = ', profit)
elif profit == 0:
    print('Фирма работает без прибыли')
else:
    print('Фирма работает с прибылью, сумма прибыли: ', profit)
    effic = profit/income
    print('Коэффициент рентабельности произодства: ', effic)
    number_workers = int(input('Введите количество сотрудников: '))
    one_worker_income = profit / number_workers
    print('Прибыль фирмы в рассчете на одного сотрудника равна: ', one_worker_income)