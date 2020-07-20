def exe_2(**kwargs):
    return list(kwargs.values())

words = (exe_2(name=input('Введите имя: '),
               surname=input('Введите фамилию: '),
               year=input('Введите год рождения: '),
               town=input('Введите город проживания: '),
               email=input('Введите email: '),
               tel=input('Введите номер телефона: ')))

words = ' '.join(words)
print(words)