'''---------списки---------'''


'''a = '   test It step Text.   '
print(a)
print(a.split()) # убирает пробелы слева и справа

a = '----It step----'
#print(a)
#print(a.center(60))
print(a.strip('-')) #strip убирает все указанные элементы слева и справа текста (lstrip/rstrip слева или справа)'''

'''a = [12, 12, 11, 12, 11, 10, 10, 10, 10]
students = ['Alex', 'Mark', 'Katy']
t = [10.2, 10.5, 10.5]
test = [12, 12, 'Text']
print(a)
print(students)
print(t)
print(test)'''

'''students = ['Alex', 'Mark', 'Katy', 'Tania']
# индексация элементов начинается с 0. Алекс- 0, Марк - 1, Кати - 2
# create line 22
# read  lines 28-32
# append добавить
# remove
# edit
# CRUD - create, read, update, delete
print(students)
print('Hi', students[0])
print('Hi', students[1])
print('Hi', students[2])
print('Hi', students[3])
print('Hi', students[0:3])
print('Hi', students[0:3])
print('Hi', students[0], students[3])
a = [12, 12, 11]
print(a[2])
# append (добавить элемент в список)
a = [12, 12, 11, 10]
print(a)
a.insert(2, '9')  # добавить элемент после индекса 2- индекс, а элемент - '9'
print(a)
a.append(9) #добавить элемент в конец
print(a)
a.extend([1, 2, 3]) #extend чтобы добавить одновременно несколько элементов в конец
print(a)
# remove

students = ['Alex', 'Mark', 'Katy', 'Tania']
print(students)
i = students.index('Katy') # найти индекс элемента
print(i, students[i]) # найти индекс элемента
del(students[2])
print(students)

# edit

ocenki = [12, 11, 10, 9]
print(ocenki)
#a=9
#a=11
ocenki[3] = 11
#ocenki[3] = 11
#ocenki[1] = 12
print(ocenki)'''

'''students = ['Alex', 'Mark', 'Katy', 'Tania']
students.append('Bob')
for item in students:
    print('Hi', item)
    print(item, [10, 11, 12])

students = ['Alex', 'Mark', 'Katy', 'Tania']
students.append('Bob')
for i in range(len(students)): # len(students) для всех элементов
    print(i, students[i])'''

'''a = [1, 2, 3, 4]
b = [5, 6, 7]
print(a)
print(b)
c = a + b
print(c)'''

# создать 2 любых списка
# вывести из первого списка второй элемент
# заменить во втором списке последний элемент. вывести

'''e_planets = ['mercury', 'venus', 'earth', 'mars']
g_planets = ['jupiter', 'saturn', 'uranus', 'pluto']

print(e_planets[1])

g_planets[3] = 'neptune'  # g_planets[-1] = 'neptune'
for planet in g_planets:
    print(planet)
print(g_planets)


solar = e_planets + g_planets
print(solar)'''

'''b = [
      #0       #1
    ['Artem', 'Mark'], #0
       #0      #1      #2
    ['Katy', 'Alex', 'Artem'], #1
]
print(b[0][0]) # первая цифра- номер списка, а вторая - элемент этого списка
print(b[0][1])

b = ['artem', 'mark']
print(len(b))
print(b[0][0])
print(b[0][1])
print(b[2])'''

'''a = [1, 2, 3, 4]
b = [5, 6, 7]
c = a + b
print(a)
a = a + b + c
print(b)
print(c)'''

'''a = [0] * 100
print(a)'''

'''a = [[12, 12, 12], ] + [[0, 0, 0, 0]] * 100
print(a)'''

'''a = ['It', 'st', 'ep']
print(a)

a[0:2] = ['IT', 'ST']
print(a)'''


'''a = [1, 2, 3, 4, 5]

a.append(6)
print(a)

L = [6, 7, 8, 9, 10]
a.extend(L)
print(a)'''

'''a = [1, 2, 3, 4, 5]
a.insert(3, 4)
print(a)'''

'''a = [1, 12, 12, 12, 1, 4, 4, 34]
a.remove(4) # удаляет первый элемент, чтобы удалить еще надо продублировать
print(a)'''

'''a = [1, 12, 12, 12, 1, 4, 4, 34]
val = a.pop(5)
print(a)
print('deleted element', val)'''


'''a = [1, 12, 12, 12, 1, 4, 4, 34, 12, 12, 12, 12]
i = a.index(4)  #если искомого нету, то выдает valueerror
print(i)
print(a[i])
i = a.index(4, 6, -4)
print(i)'''

'''a = [1, 12, 12, 12, 1, 4, 4, 34, 12, 12, 12, 12]
print(a.count(12))
print(a.count(1))
print(a.count(5))
print(0 in a)
if 0 in a:
    i = a.remove(0)
print(a)'''

'''a = [12, 1, 2, 3, 5, 11, 10]
print(a)
# a.sort() сортировка по возрастанию
# для слов - сортировка идет по алфавиту
a.sort(reverse=True) # по убыванию
print(a)
print(a[1])'''

'''a = [12, 1, 2, 3, 5, 11, 10]
print(a)
a.reverse()
print(a)'''


'''a = [12, 1, 2, 3, 5, 11, 10]
print(a)
a.clear()
print(a)'''

'''a = [12, 121212, 212122, 3435, 7878787, 1, 23, 45]
print(max(a))
print(min(a))
print(sum(a))
print(sum(a) / len(a)) # среднее арифметическое

b = sorted(a)
print(b)   
print(a)

print(sorted(a))  # сортировка с сохранением оригинального списка'''


'''a = [12, 12, 11, 9, 13]
b = a

# a[0] = 11

print(a)
print(b)

a[0] = 1

print(a)
print(b)

a = [12, 12, 11, 9, 13]
b = a.copy()

print(a)
print(b)

a[0] = 1

print(a)
print(b)'''


import random
nums = []
for i in range(100):
    nums.append(random.randint(-100, 100))
print(nums)