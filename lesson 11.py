'''Анонимные функции'''

# lambda arg1, arg2, ..., : expression

'''m = lambda a, d:a/d
print(m(4,2))'''

'''mult = lambda a, b, c: a * b * c
print(mult(5, 2, 9))
result = mult(5, 2, 9)
print(result)

def multdef(a, b, c):
    return a * b *c
print(multdef(5, 2, 9))
result = multdef(5, 2, 9)
print(result)'''


'''import math

abs = lambda a, b:math.sqrt(a * a + b * b)
result = abs(9, 7)

def absdef(a, b):
    return math.sqrt(a * a + b * b)
resultdef = absdef(9, 7)
print(result)
print(resultdef)'''

'''discr = lambda a, b, c: b * b - 4 * a * c
print(discr(3, 4, 5))

def discr_def(a, b, c):
    return b * b - 4 * a * c
print(discr_def(3, 4, 5))'''

'''import random
spisok = [lambda : random.random(),
          lambda : random.random(),
          lambda : random.random()]

for i in spisok:
    print(i())'''

'''cort = (lambda x: x * 2,
        lambda x: x * 3,
        lambda x: x * 5)

for i in cort:
    print(i(2))

for i in cort:
    print(i('qwerty'))'''

# Таблицы переходов

'''slovnyk = {1: (lambda: print('Monday')), 2: (lambda: print('Tuesday')),
           3: (lambda: print('Wednesday')), 4: (lambda: print('Thursday')),
           5: (lambda: print('Friday'))}

answer = int(input('Enter the number from 1 to 5: '))
try:
    slovnyk[answer]()
except KeyError:
    print('Wrong value!')'''

'''s = {1: 'a', 2: 'b'}
print(s[1], s[2])'''

'''import math

area = {'circle': (lambda r: math.pi*r*r),
        'rectangle': (lambda a, b: a*b),
        'trapezoid': (lambda a, b, h: (a + b) * h/2.0)}
answer = input('Enter figure: ')
if answer.lower() == 'circle':
    answer1 = int(input('Enter r'))
    print('Площадь круга = ', area['circle'](answer1))
elif answer.lower() == 'rectangle':
    answer1 = int(input('Enter a'))
    answer2 = int(input('Enter b'))
    print('Площадь прямоугольника = ', area['rectangle'](answer1, answer2))
elif answer.lower() == 'trapezoid':
    answer1 = int(input('Enter a'))
    answer2 = int(input('Enter b'))
    answer3 = int(input('Enter h'))
    print('Площадь трапеции = ', area['trapezoid'](answer1, answer2, answer3))'''


'''summ = lambda a=1, b=2, c=3: a + b + c

print(summ())
print(summ(5))
print(summ(10, 20))
print(summ(10, 20, 25))
print(summ(10, 20, 25))


def func(a = 2, b = 3):
    return a + 4 + b
print(func())
print(func(4))
print(func(5, 8))'''

'''import random

def randomNumber():
    n = random.random()
    res = lambda : int(n * 100)
    return res()

print(randomNumber())'''


'''num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number:'))

sloj = lambda num1, num2:  num1 + num2
vichi = lambda num1, num2: num1 - num2
umnoj = lambda num1, num2: num1 * num2
delen = lambda num1, num2: num1 / num2
kvadr = lambda num1: num1 * num1

act = input('Enter action- +, -, *, /, **: ')
if act == '+':
    print(sloj(num1, num2))
elif act == '-':
    print(vichi(num1, num2))
elif act == '*':
    print(umnoj(num1, num2))
elif act == '/':
    print(delen(num1, num2))
elif act == '**':
    print(kvadr(num1))
else:
    print('Wrong action!')'''

'''max = (lambda a, b: a if a > b else b)
print(max(23, 70))
print(max(21, 4))'''

'''minimum = (lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))
print(minimum(21, 34, 56))
print(minimum(34, 21, 56))
print(minimum(3, 2, 1))'''

'''def mnoj_dva(x):
    return x * 2

spysok = [6, 1, 2, 3, 4, 5, 7, 8]

spysok2 = list(map(mnoj_dva, spysok))
print(spysok2)

spysok3 = list(map((lambda x: x * 2), spysok))
print(spysok2)'''

'''cort = (2.88, -5.97, 9.78)

cort2 = tuple(map((lambda x:int(x)), cort))
print(cort2)'''

'''cort = ('qwerty', 'hello', 'abc', 'qwe', 'jkl', 'word')
cort2 = tuple(filter((lambda x: len(x)==3), cort))
cort3 = tuple(filter((lambda x: len(x)>3), cort))
print(cort2)
print(cort3)'''

'''spysok = [3, 5, 2, 12, 15, 25, 57, 150, 3, 1, 9, 60, 56, 45, 98]
spysok2 = list(filter(lambda x:(x>= 10) and (x<=60), spysok))
spysok3 = list(filter(lambda x:(x<= 10) or (x>=60) or (x==25), spysok))

print(spysok2)
print(spysok3)

def vid_10_do_30(x):
    return (x>=10 ) and (x<=30)
spysok4 = list(filter(vid_10_do_30, spysok))
print(spysok4)'''

# Регулярные выражения

'''import re
spysok_1 = 'Bob0 Anna Alice Alex Gena Bob'
spysok_2 = 'abc qwe rty gfd'

vyraz = re.compile('Bob') # compile створення рядку  который мы ищем
vyraz_2 = re.compile('qwe')
match1 = vyraz.search(spysok_1) # search позиция первого входження эелемента
print(match1)
match2 = vyraz.search(spysok_2) # search если элемент не найден то None
print(match2)
match3 = vyraz.finditer(spysok_1) # finditer найти все збИги и их позиции
for i in match3:
    print(f'match_1 - {i}')

match4 = vyraz.findall(spysok_1) # findall найти все збИги и поместить их в список
print(match4)
print(len(match4))

spysok_2 = 'abc qwe rty gfd'
poshuk = re.compile('rty')
new = poshuk.sub('HelloWorld', spysok_2) # sub замена паттерна на другое значение
print(new)'''

'''import re
rechennya = 'По всем вопросам пишите на почту qwerty-1@gmail.com, или на newadress@ukr.net, или на itstep@outlook.com'
emails = re.findall(r'[\w]+@[\w\.]', rechennya) #попробовать такой паттерн \w{3,20}@[a-z]{2,10}\.[a-z]{2,6}
# \w цифры, буквы, _ (нижнее тире)
for i in emails:
    print(i)'''

import tkinter as tk
import re
loggin_patter = re.compile(r'^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$') # ^ - начало рядка, $ - конец рядка
password_pattern = re.compile(r'^\w{8,16}$')
root=tk.Tk()
root.geometry('400x250+700+500') # размеры окна и его положение
root.resizable(False, False) # нельзя менять размер окна (справа и слева)
def logining():
    pass
login_label = tk.Label(root, text = 'Login', font=('Arial', 14), padx=50)
password_label = tk.Label(root, text='Password', font = ('Arial', 14), padx = 50)
root.grid_columnconfigure(0, minsize=150)
login_label.grid(column=0, row=0)
root.mainloop()
