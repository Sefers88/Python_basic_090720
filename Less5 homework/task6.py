subj = {}
with open('task6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по каждому предмету - \n {subj}')