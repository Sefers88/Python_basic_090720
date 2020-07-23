numbers_list = [2, 7, 7, 5, 1, 6, 1, 7, 9, 3, 5, 2] #Создаем список цифр
result_list = [el for el in numbers_list if numbers_list.count(el) < 2] #Создаем новый список в котором будут цифры без повторов из списка number_list
print(result_list)
