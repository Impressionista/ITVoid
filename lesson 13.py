# рекурсия

'''spysok = [2, 4, 7, 12, 34, 1, 56, 78, 9]'''
'''b = 0
for i in spysok:
    b += i

print(b)'''


'''def calcSum(A):
    if A == []:
        return 0
    else:
        sum = calcSum(A[1:])
        sum += A[0]
        return sum


sum = calcSum(spysok)
print(sum)'''

'''def c(t):
    return t * 2
def a(b):
    print(c(6))
    print(b)'''

'''spysok = [1, -7, 9, 15, 25, -67, -98, -56, 65]


def calcSumNegative(A):
    if A == []:
        return 0
    else:
        count = calcSumNegative(A[1:])
        if A[0] < 0:
            count += 1

        return count


n = calcSumNegative(spysok)
print(n)'''

# пройтись по каждлму из этих кодов и пропустить их через pythontutor


# фибонначи

'''def GetFibonacciList(n, L):
    count = len(L)
    if len(L) < 2:
        return []

    num1 = L[count-2]
    num2 = L[count-1]

    if (num1+num2) < n:
        L = L+[num1 + num2]
        return GetFibonacciList(n, L)
    else:
        return L

new = GetFibonacciList(100, [0,1])
print(new)'''

'''def Power(x, y):                  # 1) Power(3, 4)  .... 3*3*3*3
    if y > 0:                     # 1) 4 > 0 --->
        return x * Power(x, y-1)  # 1) 3 * Power(3, 3)
    else:
        return 1

x = 3
y = 4
res = Power(x, y)
print(res)'''

'''def GetMaxList(L):
    if len(L) > 1:
        Max = GetMaxList(L[1:])
        if L[0] < Max:
            return Max
        else:
            return L[0]
    if len(L) == 1:
        return L[0]
spysok = [500, 6000, 40, 53]
res = GetMaxList(spysok)
print(res)'''


'''def GetMinList(L):
    if len(L) > 1:
        min = GetMinList(L[1:])
        if L[0] > min:
            return min
        else:
            return L[0]
    if len(L) == 1:
        return L[0]

def countPositive(L):
    if L == []:
        return 0
    else:
        count = countPositive(L[1:])
        if L[0] > 0:
            count += 1

        return count

list = input('Enter numbers: ').split()
list = [int(num) for num in list]

result1 = GetMinList(list)
result2 = countPositive(list)

action = input('Choose action 1 to get minimum or 2 to count positive nums: ')

if action == '1':
    print(result1)
elif action == '2':
    print(result2)'''

# decorators

'''def simpledecorator(myFunction):
    print('Hello! I am Decorator!')
    def simpleWrapper():
        print('Function starts working...')
        myFunction()
        print('See you!')

    return simpleWrapper()

def simpleDecorator_v2(myFunction):
    print('Hello, I am the second decorator!')
    def simpleWrapper():
        print('Lets start ...')
        myFunction()
        print('Good luck!')
    return simpleWrapper
@simpleDecorator_v2
@simpledecorator
 # декораторы срабатывают в обратном порядке их положения в коде
def sayHi():
    print('Welcome!')
sayHi()

#new_version = simpledecorator(sayHi)
#new_version()


def sayBye():
    print('Bye!')

sayBye = simpledecorator(sayBye)
sayBye()'''


'''def simpleDecorator_v3(myFunction):
    print('I am the 3rd decorator!')
    def simpleWrapper():
        print('Function starts working...')
        result1 = myFunction()
        print('See you!')
        return result1
    return simpleWrapper

def calculateSum():
    print('Welcome! Lets start to calculate')
    x = int(input('x: '))
    y = int(input('y: '))
    return x + y

a = simpleDecorator_v3(calculateSum)
print(a())'''


def simpleDecorator_v4(myFunction):
    print('Hello! I am the fourth decorator!')
    def simpleWrapper(argX, argY):
        print('I have got {}, {}. Function starts working ...'.format(argX, argY))
        result1 = myFunction(argX, argY)
        print('See you!')
        return result1
    return simpleWrapper

def calculateSum(a, b):
    print('Welcome! Lets start to calculate')
    x = int(input('x: '))
    y = int(input('y: '))
    return x + y + a + b

a = simpleDecorator_v4(calculateSum)
print(calculateSum(3, 4))