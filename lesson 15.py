# datetime(year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0)

'''import datetime

dates = datetime.datetime(2023, 5, 23, hour=19, minute=24, second=53, microsecond=585)
print(f'object datetime = {dates}')
print(f'type-{type(dates)}')

dates = datetime.datetime(2023, 5, 23, hour=19, minute=24, second=53, microsecond=585)
print(f'method date() - {dates.date()}\n type of its result - {type(dates.date())}')
print(f'method time() - {dates.time()}\n type of its result - {type(dates.time())}')
date_1 = datetime.date(2021, 9, 24)
time_1 = datetime.time(5, 8, 48)
print(f'date = {date_1}')
print(f'time = {time_1}')
date_and_time = datetime.datetime.combine(date_1, time_1)
print(f'datetime = {date_and_time}, type date = {type(date_and_time)}')
print(f'new date = {date_1.replace(2022)}')
print(f'old date = {date_1}')'''

'''import datetime
date_now = datetime.datetime.now()
date_today = datetime.datetime.today()
date_date = datetime.date.today()
print(f'date now = {date_now}')
print(f'date today = {date_today}')
print(f'date today without time = {date_date}')

print(f'time now = {date_now.time()}')'''

#weekday
#isoweekday

'''date_for_now = datetime.datetime.now()
print(f'weekday() = {date_for_now.weekday()}')
print(f'isoweekday() = {date_for_now.isoweekday()}')'''

# %A - полное название дня недели
# %B - полное название месяца
# %d - день месяца [01, 31]
# %H - час (24 часовой формат)
# %m - номер месяца
# %M - число минут
# %S - число секунд
# %x - дата
# %X - время
# %y - год

'''import datetime

date_now = datetime.datetime.now()
print(f'date time to str = {date_now.strftime("%d.%m.%Y %H:%M:%S %A")}')

date_str = '28/09/2021 11:20'
date_str_res = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
print(f'str to datetime = {date_str_res}')'''

'''import datetime
date_now = datetime.datetime.now()
date = datetime.datetime(day=20, month=8, year=2020)
print(date_now - date)'''

'''import datetime
date_now = datetime.datetime.now()
print(f'date now = {date_now}')
delta = datetime.timedelta(days=20, hours=8, weeks=4)
print(f'delta = {delta}')
print(date_now+delta)
print(date_now-delta)
a = date_now + delta
print(f'future date = {a.strftime("%d.%m.%Y %H:%M:%S")}')'''


'''

Практическое задание

import datetime

choice = input('1- текущая дата, \n2- День недели, \n3- Время сейчас, \n4- Кол-во дней до указаной даты, \n5- Рассчитать дату\n')
if choice == '1':
    print('Текущая дата- ', datetime.datetime.now())
elif choice == '2':
    date = datetime.datetime.now()
    print('День недели-', date.isoweekday())
elif choice == '3':
    time = datetime.datetime.now()
    print('Время сейчас-', time.time())
elif choice == '4':
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    today = datetime.datetime.now()
    new_date = datetime.datetime(year, month, day)
    print('Кол-во дней до указанной даты-', today - new_date)
elif choice == '5':
    choose = int(input('Enter the amount of days: '))
    delta = datetime.timedelta(days=choose)
    today = datetime.datetime.now()
    days = today + delta
    print('Через', choose, 'дней будет- ', days)'''

# osfiles

'''import os

path = 'C:\Windows\Web'
path2 = os.path.normpath('C:/Windows/Web')
path3 = 'C:\\Windows\\teb'  # чтобы не было \n \t
path4 = r'C:\Windows\teb'   # чтобы не было \n \t
for path, dirnames, filenames in os.walk(path):
    print(f'path -{path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames -{filenames}')'''

'''import os
path = os.path.normpath('new dir')
os.mkdir(path)'''

'''import os
path = os.path.normpath('new dir')
os.rmdir(path)'''

