user_str = input("введите несколько или более слов и символов через пробел: ")
user_word = []     # Создаем список для решения задачи
num = 1            # Задаем переменную для нумерации строк при выводе информации на экран
for el in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    print(f" {num} {user_word [el] [0:10]}")     # Ограничиваем выводимые символы до 10 знаков
    num += 1       # Задаем увеличение каждой следующей строки на 1
