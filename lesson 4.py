'''
number = int(input('Enter number (up to 10): '))
while number < 10:
    print('number =', number)
    number += 2
print('The cycle has ended!')
print('----------')

number = int(input('Enter number (up to 10): '))
while True:
    print('number =', number)
    number += 2
    if number >= 10:
        break
    str = input('Do you wish to continue? ')
    if str == 'No' or str == 'N':
        break
'''

'''
import random
# a) from random import randint
print('The game - Guess the number!')
bot_number = random.randint(1, 10) # a) bot_number = randint(1, 10)
num_2 = 0
while True:
    num_2 += 1
    user_number = int(input('Enter the number /up to 10/: '))
    if user_number > bot_number:
        print('Your number is bigger than bot`s number!')
    elif user_number < bot_number:
        print('Your number is smaller than bot`s number')
    elif user_number == bot_number:
        print('You have won!')
        break
    if num_2 > 2:
        print('You have spent all the attempts!')
        break
print('The game is over!')
print(f'The guessed number is - {bot_number}')
print(f'You have guessed {num_2} times!')
'''

'''import random
bot_number = random.randint(1, 10)
user_number = 0
while True:
    while bot_number != user_number:
        user_number = int(input('Enter the number: '))
        if user_number > bot_number:
            print('Your number is bigger than bot`s number!')
        elif user_number < bot_number:
            print('Your number is smaller than bot`s number')
        elif user_number == bot_number:
            print('You have won!')
        print('The game is over!')
        print(f'The guessed number is - {bot_number}')
        str = input('Do you want to continue? / Y or N - ')
        if str == 'Y' or str == 'y':
            bot_number = random.randint(1, 10)
        else:
            break
    print('OK!')


while ...:
# если нет break то выполняется блок дальше else:
else:'''

'''number = input('Введите целое число: ')

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print('Не верно введено число!')
        number = input('Введите целое число: ')

print('Ok!')
'''

''' print(eval('5 + 5 ** 2')) ''' #eval - анализ строки и проведение подсчетов строки

# for - цикл

'''x = 5

for i in 2, 3, 4, 5:
    x += i
    print(f'{i} --> x = {x}')'''

'''x = 5
for i in range(5):   # range(n) - где n = количество повторов . i --> 0, 1, 2, 3, 4
    x += 5
    print(f'{i} --> x = {x}')'''


'''for i in range(1, 11, 3): #каждый второй элемент пропускается
                          # (если 1(включительно), 11(не включительно)
                          # 3 - то пропускается каждый 3)
    print('i - ', i, end= ' ')
    if i % 2 == 0:
        print('Четное \n')
    else:
        print('Нечетное \n')
    #print(' \n')'''

'''
str = 'strings'  # len - считает количество символов в строке
print(len(str))
print(str[0])
print(str[-7])
x = 0
for i in range(len(str)): # for i in range(7):
    print(str[i])

lst = [27, 'mama', ['papa', 56], 67]
for i in lst:
    print(i)
print(lst[2][0])


str_1 = input('Enter some string- ')
for i in str_1:
    print(str_1)
    
line = input('Enter some string- ')
for c in line:
    print(c)
    

str = 'mamapapa'
print(str[0:4])
print(str[:4])
print(str[:4:2])

line = input('Enter some string: ')
for c in line[0:6:2]:   #[::2] - :: это от начала до конца
    print(c)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'i*j= {i * j}', end='\t')
    print('\n')


floor = 1
energy = 20
while floor != 5:
    print('You are on the ', floor, 'floor')
    step = 0
    while step != 20:
        step += 1      # step = step + 1
        energy -= 1
        if energy == 0:
            print('You need to have a rest!')
            energy += 20
    floor += 1
    print('You are on the ', floor, 'floor')
print('floor = 5')
'''



