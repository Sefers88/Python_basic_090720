def my_func(x, y, z):
    order = [x, y, z]
    total = []
    max_1 = max(order)
    total.append(max_1)
    order.remove(max_1)
    max_2 = max(order)
    total.append(max_2)
    print('Cумма двух наибольших чисел = ', sum(total))

my_func(19,4,-42)
