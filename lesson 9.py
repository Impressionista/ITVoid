'''student = ['Bob', 19, 95] # name, age, score
template = "Name: {}; age: {}; scores{}"
users = ['admin', 'teacher', 'manager']
while True:
    print('1-print info')
    print('2-modify info')
    print('3-exit')
    userChoice = input('Select menu item: ')
    if userChoice == '1':
        user = input('Login: ')
        if user in users:
            print('Current information: ')
            print(template.format(student[0],
                                  student[1],
                                  student[2]))
    elif userChoice == '2':
            user = input('Login: ')
            if user in users:
                print('Current information: ')
                print(template.format(student[0],
                                        student[1],
                                        student[2]))
                userAnsw = input('Change this info y-n?')
                if userAnsw == 'y':
                    name = input('Input name:')
                    age = input('Input new age:')
                    scores = input('Input new score:')
                    student[0] = name
                    student[1] = age
                    student[2] = scores
                    print(template.format(student[0],
                                          student[1],
                                          student[2]))
    elif userChoice == '3':
        print('Bye!')
        break
    else:
        print('Error: wrong menu item')'''
import math

'''help(breakpoint)'''

#math.имя функции(...)
#ceil возвращает ближайшее целое значение (округлення в гору)
#floor возвращает ближайшее целое значение (округлення вниз)
'''import math
a = 0.23
b = 1.87
c = 3
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))

print(math.floor(a))
print(math.floor(b))
print(math.floor(c))

#modf() - повертае дробную и целую часть числа
x = 2.49
y = 1.5
print(math.modf(x))
print(math.modf(y))

#trunc() - отримання целой части числа
x = 2.45
y = 1.5
print(math.trunc(x))
print(math.trunc(y))

#abs - возвращает модуль числа с тем самым типом вИхидне число (используется без math)
#fabs - возвращает модуль числа с типом float

q = -2
w = -2.5
e = 4
print(math.fabs(q))
print(math.fabs(w))
print(math.fabs(e))

print(abs(q))
print(abs(w))
print(abs(e))

#factorial - факториал 4 != 4*3*2*1=24, если число не целове - ValueError или Type Error
p = 4
e = 7.4
try:
    print(math.factorial(p))
    print(math.factorial(e))
except TypeError:
    print('Not correct item!')'''

#randint(a,b) - принимает только 2 аргумента и из этого диапазона випадкове число
# первое число всегда должно быть меньше второго

'''import random
for i in range(3):
    print('step', i+1)
    print(random.randint(1,5))
    print(random.randint(-3,20))
    print(random.randint(-10,-6))'''

# randrange() - от одного до трех аргументов
# randrange(a) - випадкове число от 0 до указанного [0;a) от нуля до a-1
# randrange(a,b) - аналогично randint, но верхняя граница не входит в диапазон. [a:b) от a до b-1
# randrange(a,b,c) - первые два числа это границы диапазона, третье ход генератора. (10, 18, 2) 10, 12, 14, 16

'''import random
for i in range(3):
    print('Step', i+1)
    print(random.randrange(10))
    print(random.randrange(-4, 3))
    print(random.randrange(10, 20, 3)) # 10 13 16 19'''

#random - вызов без аргументов, випадкове число генеруется в диапазоне от 0 до 1, но не включая один

'''import random
for i in range(3):
    print('step', i+1)
    print(random.random())'''

#choice(L) - L- это последовательность или ее имя. Функция для
'''import random
L = [1, 24, 'Bob', True, False, 7.9, 'hello']
for i in range(3):
    print(random.choice(L))
    print(random.choice(['red', 'blue', 'green', 'white']))'''

'''a = int(input('Enter the number: '))
act = input('Factor, Abs, Random, Random R, Modf')
import math
import random
if act == 'Factor':
    print(math.factorial(a))
if act == 'Abs':
    print(abs(a))
if act == 'Modf':
    print(math.modf(a))
if act == 'Random':
    print(random.randint(0, 100))
if act == 'Random R':
    od = input('1')
    dv = input('2')
    print(random.randrange(od, dv))
#Пользователь может запросить у программы: определить факториал, придать абсолютное значение, сгенерировать случайное число от 1 до 100, сгенерировать случайное число из самостоятельно заданного диапазона, получить целую и дробную части числа
'''


# def имя(): начинается с буквы или _, состоит тлько из букв, цифр или _
'''def printMsg():
    print('Hello')
    print('Welcome')
printMsg()
print('Bye!')'''

'''def printMsg1(myMsg):
    print(myMsg)

def printMsg2(myMsg1, myMsg2):
    print(myMsg1)
    print(myMsg2)

myMsg1 = 'Hello'
myMsg2 = 'World'
printMsg2(myMsg1, myMsg2)'''

'''def calculate(a, b, c):
    print('lets calculate')
    print(a + b * c ** 2)

q = 5
w = 2
e = 3
calculate(q, w, e)
calculate(q, w, 3)
calculate(5, 2, 3)'''

'''def modifyName(userName):
    newName = userName.upper()
    return newName
    print('Hello')
name = input('input your name:')
print(modifyName(name))
print(f'User name:{modifyName(name)}')
a = modifyName(name)
b = a + '.Hello user'
print(b)'''

'''def calculate(a, b):
    return a + b
a = float(input('input a:'))
b = float(input('input b:'))

if calculate(a,b) <= 0:
    y = 5*a+2*b
else:
    y = 10*a - 3*b

print('y =', y)'''

'''def checkCustomer(customer, customers):
    result = 0
    print('Clients positions in the list:')
    for i in range(len(customers)):
        if customers[i]==customer:
            print(i)
            result+=1
    return result
customerList = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
myCustomer = input('Enter name:')
if checkCustomer(myCustomer, customerList) > 1:
    print(f'Customer {myCustomer}, will get a discount')'''

'''def modifyName2(userName):
    newName1 = userName.upper()
    newName2 = userName.lower()
    return newName1, newName2
name = input('Enter your name:')
print(modifyName2(name))
nameUpper, nameLower = modifyName2(name)
print(nameUpper)
print(nameLower)'''

'''def checkLog(userLog):
    if userLog == 'admin':
        return userLog.upper()
    elif userLog.lower() == 'user':
        return userLog.lower()
    else:
        return 'Wrong login'

login = input('Enter your login: ')
print(checkLog(login))'''

'''def meanF(*args):
    s = 0
    k = 0
    for i in args:
        s += i
        k += 1
    return s/k

print('(1+5+7)/3 = ', meanF(1, 5, 7))
print('(1+5+7+4+9+12+13)/7 = ', meanF(1, 5, 7, 4, 9, 12, 13))'''

'''def userGreetings(login, passw='111'):
    if login == 'admin':
        print('Welcome, admin!')
        print(passw)
    elif login == 'student':
        print('Welcome student!')
    else:
        print('Welcome. IDK who you are...')

userGreetings('admin')
userGreetings('admin', 'qwerty')'''

'''def a(a, b, c):
    print(a, b, c)

a(1, 2, 3) # позиционные аргументы'''

def calcBMI(m, h):
    return m/(h**2)

print(calcBMI(h = 1.6, m = 50)) # именной
print(calcBMI(50, 1.6)) #позиционный