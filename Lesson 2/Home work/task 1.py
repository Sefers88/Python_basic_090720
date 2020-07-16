str = "Игорь Игорь Арбузы Арбузы"
int = 670
float = 3.214
list = ['Лес', 'Карнавал']
tuple = ('кортеж', 'уехал')
dict = {'key1': '2', 'key2': '4'}

list_in_list = [str, int, float, list, tuple, dict]
for i in list_in_list:
    print(f'{i} is {type(i)}')
