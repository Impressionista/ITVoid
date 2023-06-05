# OOP

'''def checkStudentSuccess(name, score):
    if score >= 90:
        print(f'{name} has excelent level')
    elif 75 <= score < 90:
        print(f'{name} has good level')
    elif 60 <= score < 75:
        print(f'{name} has normal level')
    else:
        print(f'{name} has bad level')

def checkPupilSuccess(name, score):
    if score >= 10:
        print(f'{name} has excelent level')
    elif 7 <= score < 10:
        print(f'{name} has good level')
    elif 4 <= score < 7:
        print(f'{name} has normal level')
    else:
        print(f'{name} has bad level')

checkStudentSuccess('Jane', 78)
checkPupilSuccess('Bob', 6)'''


'''userLogs = ['Admin123', 'superUser', 'GoodStudent']
userBYears = [2000, 2010, 2005]

def listMaker1(mylist):
    result = []
    for item in mylist:
        result.append(item.lower())
    return result

def listMaker2(mylist):
    result = []
    for item in mylist:
        result.append(2023 - item)
    return result

newList1 = listMaker1(userLogs)
newList2 = listMaker2(userBYears)

print(newList1)
print(newList2)'''

# инкапсуляция

'''class Student: # название класса всегда с большой буквы
    age = 20
    name = 'Bob'

print('student 1 info')
student1 = Student()
print(student1.name)
print(student1.age)

print('student 2 info')
student2 = Student()
print(student2.name)
print(student2.age)'''

'''class Student:
    navch_zaklad = 'ItStep'
    spec = 'Python'
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('Bob', 20)
student2 = Student('Jane', 18)

print('student 1 info')
print(student1.age)
print(student1.name)
print(student1.navch_zaklad)
print(student1.spec)

print('\nstudent 2 info')
print(student2.age)
print(student2.name)
print(student2.navch_zaklad)
print(student2.spec)'''


class Programmer:
    mova_program = 'Python'

    def __init__(self, name, dodatkova_mova, level):
        self.name = name
        self.dodatkova_mova = dodatkova_mova
        self.level = level

    def showInfo(self):
        return f'Programmer {self.name}. \n' \
               f'Main programming lang- {self.mova_program}\n' \
               f'Dodatkova mova- {self.dodatkova_mova}\n' \
               f'Level- {self.level}'

    def showProgress(self, progress):
        return f'Programmer {self.name} made {progress}% of work.\n'

programmer1 = Programmer('Alex', 'JS', 'Senior')
programmer2 = Programmer('Anna', 'C++', 'Middle')
programmer3 = Programmer('Nick', 'Java', 'Junior')

print(programmer1.showInfo())
print(programmer1.showProgress(95))

print(programmer2.showInfo())
print(programmer2.showProgress(98))

print(programmer3.showInfo())
print(programmer3.showProgress(60))


