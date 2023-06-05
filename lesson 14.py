# файлы

# двойные файлы - документы и электронные табилицы  .doc, .pdf, xls, ...
# архивы .zip, .7z, .rar, .iso, ...
# базы данных .db, mdb, .sqllite, .accde, ...
# исполняемые файлы .exe, .dll, ...
# изображения  .png, .jpeg, .gif
# аудио .mp3, .mka
# видео .mp4, .avi

# текстовые файлы
# текстовые документы .txt, .rtf, .tex
# файлы початковых кодов .py, .js, .java, .c, .cpp
# web документы и стандарты .JSON, .HTML, .CSS, .XML
# файлы налаштувань и конфигураций .cfg, .ini

# Открыть
# Чтение
# Запись
# Удаление

# fileObj = open(fileName, mode)
# r
# w
# a
# r+
# w+
# a+
# rb
# wb
# ab
# wb+
# ab+

'''f1 = open('D:\\PY files\\p33.txt', 'r')

s1 = f1.readline()  # .readline - прочитать только 1 строку
print(s1)

s2 = f1.readline()
print(s2)'''

'''f1 = open('D:\\PY files\\p33.txt', 'r')
#print(f1.read())  # .read - чтение всего содержимого файла (работает 1 раз)
print(f1.read(4))  # read(n) - n- количество символов для чтения
print(f1.read())'''

'''f1 = open('D:\\PY files\\p33.txt', 'r')
lines = f1.readlines() # считать файл в список строк
print(lines)'''

'''f1 = open('D:\\PY files\\p33.txt', 'r')
for line in f1:
    print(line)'''

'''f2 = open('D:\\PY files\\p33_2.txt', 'w')
n = f2.write('Some text')'''

'''import random
i = 0
spysok = []
while i < 10:
    chislo = random.randint(0, 1001)
    spysok += [chislo]
    i += 1
print(spysok)

f = open('D:\\PY files\\spysok.txt', 'w')
s = str(len(spysok))
f.write(s + '\n')
for i in spysok:
    s = str(i)
    f.write(s + ' ')
f.close()'''

'''f = open('D:\\PY files\\spysok.txt', 'r')
lines = f.readlines()
print(lines)'''

'''spysok_txt = ['asdasd', 'dasdqq', 'ds2123']
f = open('D:\\PY files\\spysok_strok.txt', 'w')

for line in spysok_txt:
    f.write(line + '\n')

f.close()'''


'''slovnyk = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
f = open('D:\\PY files\\slovnyk.txt', 'w')f = open('D:\\PY files\\slovnyk.txt', 'w')
for item in slovnyk:
    s = str(item)
    s += ':'
    s += slovnyk.get(item)
    s += '\n'
    f.write(s)

f.close()'''

'''f1 = open('D:\\PY files\\p33.txt', 'r')
count = 0
s = f1.readline()
while s != '':
    s = f1.readline()
    count += 1
print(count)'''

'''f2 = open('D:\\PY files\\p33.txt', 'r')
spysok = f2.readlines()
count = len(spysok)
print(count)'''

'''f3 = open('D:\\PY files\\python.txt', 'r')
s = input('Enter text for change: ')
pos = 2
spysok = f3.readlines()
if (pos >= 0) and (pos < len(spysok)):
    if (pos == len(spysok)-1):
        spysok[pos]=s
    else:
        spysok[pos] = s + '\n'
f3.close()
f3 = open('D:\\PY files\\python.txt', 'w')
for line in spysok:
    f3.write(line)
f3.close()'''

'''pos = int(input('pos = '))
f = open('D:\\PY files\\python.txt', 'r')
spysok = f.readlines()
if (pos >= 0) and (pos < len(spysok)):
    i = pos
    while i < len(spysok)-1:
        spysok[i] = spysok[i + 1]
        i += 1
    spysok = spysok[:-1]
f.close()
f = open('D:\\PY files\\python.txt', 'w')
for line in spysok:
    f.write(line)
f.close()'''

'''f1 = open('D:\\PY files\\p33.txt', 'r')
f2 = open('D:\\PY files\\p33_2.txt', 'r')

l1 = f1.readlines()
l2 = f2.readlines()
l3 = l1 + ['\n'] + l2

f1.close()
f2.close()

f3 = open('D:\\PY files\\union.txt', 'w')
for i in l3:
    f3.write(i)
f3.close()'''


user_text = input('Enter your text: ')

f = open('D:\\PY files\\notepad.txt', 'w')

f.write(user_text)

f.close()

action = input('Would you like to create new file, edit, delete, merge?: ')

if action == 'create new file':
    f1 = open('D:\\PY files\\newNotepad.txt', 'w')

elif action == 'merge':
    list1 = f.readlines()
    list2 = f.readlines()
    list3 = list1 + list2

elif action == 'edit':
    pos = int(input('pos = '))
    f = open('D:\\PY files\\notepad.txt', 'r')
    spysok = f.readlines()
    if (pos >= 0) and (pos < len(spysok)):
        i = pos
        while i < len(spysok) - 1:
            spysok[i] = spysok[i + 1]
            i += 1
        spysok = spysok[:-1]
    f.close()
    f = open('D:\\PY files\\notepad.txt', 'w')
    for line in spysok:
        f.write(line)
    f.close()

elif action == 'delete':
    pos = int(input('pos = '))
    f = open('D:\\PY files\\notepad.txt', 'r')
    spysok = f.readlines()
    if (pos >= 0) and (pos < len(spysok)):
        i = pos
        while i < len(spysok) - 1:
            spysok[i] = spysok[i + 1]
            i += 1
        spysok = spysok[:-1]
    f.close()
    f = open('D:\\PY files\\notepad.txt', 'w')
    for line in spysok:
        f.write(line)
    f.close()
else:
    print('Wrong action!')