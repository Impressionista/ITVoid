# Ассоциативные массивы, хэш-функции

'''myDict = {'key1' : 1, 'key2': 2, 'key3': True}
myDict2 = {1: 'student', 2: 'admin'}
print(myDict)
print(myDict2)

A = {}
print('A = ', A)
B = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu'}
print(B)
print(B[2])

dict_val = {'Pi':3.1415, 'Exp':1.71}
print(dict_val)
print(dict_val['Exp'])

slovnyk_nabir = {'spysok1': [1, 2, 'hello'], 'spysok2': [8, 10, False]}
print(slovnyk_nabir)
print(slovnyk_nabir['spysok1'])'''

'''pustiy_slovnik = dict()
print(pustiy_slovnik)
week = dict(Monday=1, Tuesday=2, Wednesday=3)
print(week)
print(week)

Days = [1, 2, 3]
days_names = ['Mon', 'Tue', 'Wed']
all_days = dict(zip(Days, days_names))
print(all_days)

pairs_dict = dict([(1, 'Winter'), (2, 'Summer'), (3, 'Spring')])
print(pairs_dict)'''

'''week = dict(Monday=1, Tuesday=2, Wednesday=3)
value = week['Monday']
print(value)

pairs_dict = dict([(1, 'Winter'), (2, 'Summer'), (3, 'Spring')])
print(pairs_dict[2])'''

'''slovnyk = {1:'Python', 2:'C++', 3:'C#', 4:'SQL'}
#a = slovnyk[1]
#print(a)
lang = int(input('Enter your lang: '))
if lang in slovnyk:
    print('Lang is:', slovnyk[lang])
else:
    print('Error')

lang = int(input('Enter your lang: '))
try:
    print('Lang is:', slovnyk[lang])
except KeyError:
    print('Not correct key!')

lang = int(input('Enter your lang: '))
print(slovnyk.get(lang))'''

'''slovnyk_1 = {'programmer1':'Python', 'programmer2':'C++'}
slovnyk_2 = {'workers':slovnyk_1}
print(slovnyk_1)
print(slovnyk_2)

slovnyk_3 = {'workers':{'programmer1':'Python', 'programmer2':'C++'}}
print(slovnyk_3)'''

# len функция?

'''slovnyk_1 = {'programmer1':'Python', 'programmer2':'C++'}
print(len(slovnyk_1))

position = {'Admin':{'Admin1', 'Admin2', 'Admin3}, 'Programmers':{'Python', 'C++'}}'''

'''days = {1:'Python', 2:'C++'}
print(days[1])
days[2] = 'C#'
days[3] = 'SQL'
print(days)
del days[3]
print(days)'''

'''words = dict()
count = int(input('How many words? '))
i=0
while i < count:
    key = input('Enter key: ')
    znachenie = input('Enter value: ')

    if key not in words:
        words[key] = znachenie
    i += 1
print(words)'''


'''diction = {1:'1', 2:'2'}
print(diction)
diction.clear() #удаление элементов в середине словаря
print(diction)

diction1 = {'A':1, 'B':2}
d2=diction.copy() #создать копию словаря
print(diction1)
print(d2)
diction1['C']=3
d2['A']='one'
print(diction1)
print(d2)

d3=dict.fromkeys([1, 2, 3])#создать новый словарь из ключей
print(d3)
d4 = dict.fromkeys([1, 2], 'A')
print(d4)

d5 = dict.fromkeys([1, 2], ['A', 'B'])
print(d5)

d6 = {'1':'o', '2':'b'}
n = d6.items() # список пар ключ-значение
print(n)
n2 = dict.items(d6)
print(n2)


d7 = {1:'a', 2:'b'}
n3 = d7.keys() #список ключей
print(n3)
n4 = iter(d7)
print(list(d7))
n5 = d7.values() # список значений
print(list(n5))

d8 = {1:'a', 2:'b', 3:'c', 4:'d'}
item = d8.pop(2) # удалить элемент словаря и выводим(записываем его в переменную) его значение
print(item)
print(d8)

d9 = {1:'a', 2:'b', 3:'c', 4:'d'}
item = d9.popitem()

d10 = {'1':'A', '2':'B'}
item2 = d10.popitem() # удаляет последюю пару из словаря и записывает ее в переменную

print(item)
print(item2)

print(d9)
print(d10)

d11 = {'R':1, 'B':2, 'G':3}
item = d11.setdefault('G')
print(item)
print(d11)
item2 = d11.setdefault('W')
print(item2)
print(d11)

item3 = d11.setdefault('H', 8)
print(item3)
print(d11)

d12 = {'A':1, 'B':2}
d12.update([('C', 3), ('D', 4)])
print(d12)
d12.update([('C', 15), ('D', 24)])
print(d12)'''


'''users = [{'name':'Anna', 'age':10, 'login':'user56'},
         {'name':'Mark', 'age':21, 'login':'user123'},
         {'name':'Jack', 'age':30, 'login':'us54'},
         {'name':'Alice', 'age':16, 'login':'userAlice'}]
keyName = input('Input info type: ')
keyValue = input('Input info value: ')
if keyName == 'age' and keyValue.isdigit() == True:
    keyValue=int(keyValue)
isElementFount = False
for user in users:
    if user.get(keyName) == keyValue:
        print('Element is found!')
        for key, val in user.items():
            print('{}:{}'.format(key, val))
        isElementFount=True
        break
if isElementFount==False:
    print('Element is not found!')'''


my_dict = {'Nick':{'phone':'123456', 'telegram':{'offcial':'nick_321', 'private':'@nick_123'}, 'instagram':'nick_in'},
           'Ann':{'phone':'12345', 'telegram':{'official':'@ann_321', 'private':'@ann_123'}, 'instagram':'ann_st'},
           'Jane':{'phone':'1234', 'telegram':{'official':'@jane_321', 'private':'@jane_123'}, 'instagram':'jane_ag'}}
name = input('Enter Name: ').title()
contact_type = input('Enter the contact type: ').lower()
try:
    if contact_type == 'telegram':
        type_tg = input('private or official: ').lower()
        user = my_dict[name][contact_type][type_tg]
        print(user)
    else:
        user = my_dict[name][contact_type]
        print(user)
except KeyError:
    print('You have entered not correct info!')