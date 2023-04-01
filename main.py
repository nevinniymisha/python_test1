'''def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4)) '''

'''d = int(input())
h = int(input())
def a(b,c):
  g = b * c
  print(g ** 2)
a(d,h)'''
'''import re

a = 'AD/ACAD/ACAD/ACAD/ACAD/ACAD/AC'
b = re.split('/', a)
print(b)'''

'''n = {1, 2, 3, 4, 5, 6, 7}
n2 = {2, 12, 3, 25, 568, 10021839}
n3 = n2.copy()

print(len(n3))'''

'''n = frozenset({1, 2, 3, 4, 5, 6, 7})
try:
    n.add(8)
    print(n)
except:
    print('can\'t')'''

'''while True:
    def test(text):
        return text[::-1]
    a = input('write string:')

    print(test(a))'''




'''def test_tow():
    print("hello")'''

'''m = test(a="hi", b=15)
print(m)'''

'''from itertools import product
a={1, 2}
print((list(product(range(3), a))))'''


'''nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print((list(nums)))'''
'''a,b,c = int(input()),input(),int(input())

def x(a, b, c):
    if b == '+':
        print(a + c)'''


'''def calc(x):
    return x * 4, x ** 2


side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))'''


'''def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(2, 3))'''

'''
class A:

    def __init__(self, one, two):
        self.one = one
        self.two =  two

    def test(self):
        print( self.one ** self.two)

some = A(3, 2)
some.one = 10
some.test()'''
'''House1 = House("Robochay", 22)
House2 = House("Robochay", 24)


House1.age_of_house(5)
print(House1.age)'''
'''
class House():
    """опісаніе дома"""
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0
    def build(self):
        """строить дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")
    def age_of_house(self, year):
        """возраст дома"""
        self.age += year
class Prospect_House(House):
    """дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = Prospect_House("Поля", 5)
print(PrHouse.number)
'''
'''class Point:
     color = 'red'
     circle = 2
print(Point.__dict__)
'''
"""
class A:
     def __init__(self, name, lastname):
          self.name = name
          self.lastname = lastname
     def registration(A):
          print(name, lastname)
          (a, b)
a = input()
b = input()
"""
'''def array_diff(a, b):
    c = set(a) - set(b)
    print(list(c))

array_diff([1, 2, 3],[1, 3])'''
'''
#sorted
num = [1, 2, 6, 3, 9, 7]
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j +1], num[j]
print(num)'''
'''
name = 'Misha'
age = 17
print(f'I\'m {len(name)} I {age }')'''
'''def p():
    g = input("f")
    if g == '+':
        ()

    def func(a, c):
        print(a + c)
    func(int(input('n1:')),int(input('n3:')))'''
'''class A:
    def a(self, name , lastname):
        self.name = name
        self.lastname = lastname
    def b(self, job):
        self.job = job

     print(a.class A())
'''
#factorial
'''
def fact(x):
    if x == 1:
        return 1
    return fact(x - 1)* x
print(fact(10))
'''
#fibonachy nums
'''
while 1 == 1:
    def fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n -1) + fib(n - 2)
    print(fib(int(input())))
'''

'''
while 1 == 1:

    def pal(n):
        if len(n) <= 1:
            return True
        if n[0] != n[-1]:
            return False
        return pal(n[1:-1])

    print(pal(input()))
'''
# while 1 == 1:
#
#     def rec(s):
#         if s == 1:
#             return 1
#         return rec(s - 1) * s
#     try:
#
#         print(rec(int(input())))
#
#     except:
#         print('write int')
# a = int(input("write num:" ))
# def g(x):
#     if x == a:
#         print()
# g(int(input()))

# try:
#     while True:print(eval(input("--")))
#
# except:
#     while True:print(eval(input("--")))
# def a(num1,num2):
#     return num1 / num2
# a(2,3)