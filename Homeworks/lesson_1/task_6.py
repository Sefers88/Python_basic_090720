start_km = int(input('Введите количество километров которые вы пробежали в первый день: '))
max_km = int(input('Введите километраж который вы хотите преодолеть: '))
result_days = 1
result_km = start_km
while result_km < max_km:
    start_km = start_km + 0.1 * start_km
    result_days += 1
    result_km = result_km + start_km
print(f"Вы достигните требуемого результата на %.d день" % result_days)
