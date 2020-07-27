test_file1 = open('testTask1.txt', 'w')
line = input('Введите текст: ')
while line:
    test_file1.writelines(line)
    line = input('Введите текст: ')
    if line == ' ':
        break
test_file1.close()

test_file1 = open('testTask1.txt', 'r')
content = test_file1.readlines()
print (content)
test_file1.close()
