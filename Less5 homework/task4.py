rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('task4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(f' {new_file[0]} {new_file[1]} {new_file[2]} {new_file[3]} ')

with open('task4_final.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
