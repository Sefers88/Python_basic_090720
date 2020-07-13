time = int(input('Введите желаемое количество секунд для конвертации в часы и минкты: '))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60
if minutes < 10:
    minutes = str('0'+minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str('0'+seconds)
else:
    seconds = str(seconds)
print(str(hours)+':'+str(minutes)+':'+str(seconds))
