'''
from operator import add, sub
f = sub
print(f(2,3))
'''

'''
for i in range(0):          #nothing output
    print(i)
'''

'''
f = lambda x: x + 1         #lambda x, y: x + y...
print(f(2))
'''

'''
def summation(n):           #recursion
    if n == 0:
        return 0
    return n + summation(n-1)
print(summation(100))
'''

'''
x = 12
def f():
    x = 10          # define a new variety instead of change the global x
    def g(y):
        return y + 10
    return g

print(x)
rub = f()(12)
print(x)

'''
'''
x = 12
def add():
    x += 1
add()
print(x)
'''
'''
x1 = 1
x2 = 2
i = 2
print(x{i})
'''
'''
a = b = 1
b += 1
print(b)
'''
def f(*agus):
    return sum(agus)
x = 5
y = 4
tpe = (x, y)
print(f(tpe))

def caller(func, *args):
    return func 
return caller(func)