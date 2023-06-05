'''myStr = 'hello'
print(id(myStr)) # id - идентификатор
print(type(myStr))
print(myStr)

var_ryadok = 'Hello 1
              Hello2
Hello3'
print(var_ryadok)


a = 'Python'
print(a[0])
print(a[1])
print(a[-1])
print(a[len(a)-1])'''

'''a = 'Hello'
b = 'World'
print(a + b)
print(a * 5)

a = 'Python is a high-level, general-purpose programming language. Python Its design philosophy emphasizes code readability with the use of significant indentation via Python the off-side rule.'
print(a.capitalize())  # capitalize: первый символ - верхний регистр, а другие - в нижний
print(a.lower())  # все символы в нижний регистр
print(a.upper())  # все символы в верхний регистр
print(a.title())  # первые символы каждого слова в верхний регистр, все остальные в нижний
print(a.swapcase())  # смена на противоположный регистр

print(a.count('Python')) # ищет сколько раз повторяется фрагмент в строке
print(a.count('Python', 10, 25)) # ищет сколько раз повторяется фрагмент в строке с 10 до 25 символов
print(a.count('Python', 10)) # c 10 и до конца

print(a.find('Python')) # индекс первого символа нужного фрагмента
print(a.find('Python', 10)) # начиная с 10 символа
print(a.find('Python', 10, 15)) #  10 по 15 символ ( -1, если не находит)

print(a.index('Python')) # работает как find, но вместо -1 выводит ошибку ValueError
try:
    print(a.index('Python', 10, 15))
except ValueError:
    print('Can`t find the fragment')
finally:
    print('Thank you for using our search engine!')

print(a.rfind('Python')) # индес последнего упоминания искомого фрагмента, начиная с конца
print(a.rfind('Python', 10, 160))  # r - reverse

print(a.rindex('Python', 1, 24))  # ValueError


text = 'Крестовые походы — серия религиозных военных походов XI—XV веков из королевств Западной Европы, инициированных и направляемых Латинской церковью против мусульман, язычников и еретиков.'
act = input('Введите слово для поиска в тексте: ')
try:
    print('Ваше слово начинается на', text.find(act), '')
except ValueError:
    print('Такого слова нет в тексте!')
finally:
    print('Спасибо, что воспользовались нашим поиском!')
    
zminna = ('найчастіше вживане прочитання')
word = input('enter: ')

if word in zminna:
print('find!')
else:
print('nope')
'''
'''
a = 'Python is a high-level, general-purpose programming language. Python Its design philosophy emphasizes code readability with the use of significant indentation via Python the off-side rule.'
print(a.startswith('p')) # начинается ли строка с заданного фрагмента true или false
print(a.startswith('P'))
print(a.startswith('Python'))
print(a.startswith('P', 90))

print(a.endswith('.')) # завершается ли строка заданным фрагментом
print(a.endswith('n', 0, 6))
print(a.endswith('.', 0, 6))

str = 'Python2023'
print(str.isalnum())  #состоит ли строка из букв и чисел
print(str.isalpha())  #только из букв
print(str.isdigit())  #только из чисел'''

'''a = input('Enter 1st number: ')
b = input('Enter 2nd number: ')
if a.isdigit() == True and b.isdigit() == True:
    c = int(a) + int(b)
    print(c)
else:
    print('Wrong value!')'''

'''str = 'hello'
print(str.islower()) #проверяет если все элементы строки в нижнем регистре
print(str.istitle()) # если каждое слово начинается с большой буквы
print(str.isupper()) # если все элементы строки в верхнем регистре

str_1 = '\n\t\n      \n'
print(str_1.isspace()) #только символы пробела- пробел, \n, \t'''

'''str = 'Pyt\thon'
print(str.center(30))
print(str.center(30, '*'))
print(str.center(50, '-'))
print(str.expandtabs(tabsize=8)) #сколько пробелов в табуляции \t
print(str.ljust(30, '@'))
print(str.rjust(30, '0'))'''

'''str = 'Python-cool!'
print(str[1:3])
print(str[-5:-2])
print(str[-5:11])
print(str[0:6])
print(str[:])
print(str[-5:])
print(str[7:])

str_1 = '0123456789'
print(str_1[2:10:2])
print(str_1[9:2:-2])
print(str_1[::-1])
print(str_1[5::2])
print(str_1[-1::-2])
print(str_1[:len(str_1):3])'''

'''a = r'\n- newline'  #r или R для того, чтобы не экранировался текст строки
print(a)
b=r'\t\tAddition+\n'
print(b)
c = r'\\'
print(c)
d = r'abc\\\ '  #нельзя заканчивать подряд
print(d)'''

'''day = 11
month = 'April'
year = 2023
print('Today is {}.{}.{}'.format(day, month, year))
print('Today is {day}.{month}.{year}'.format(month=4, day=11, year=2023))'''

'''name = 'Ali'
year = 2023
print(f'Hello, {name}')
print(f'Hello, {name:^30}')
print(f'Hello, {name:<30}')
print(f'Hello, {name:-^30}')
print(f'Hello, {name:>30}')
print(f'Hello {name*2}')
print(f'Hello, {len(name)}. Now is {year}')
# ^ выравнивание по центру
# < по левому краю
# > по правому краю'''

'''number = input('Введите число: ')
product = 1
for i in number:
    product *= int(i)
print('Произведение введенных чисел равно:', product)'''

a, b, c, d = map(int, input().split())
product = a * b * c * d
print(product)

a = int(input('number: '))
b=a%10
print(b)
a=a//10
print(a)