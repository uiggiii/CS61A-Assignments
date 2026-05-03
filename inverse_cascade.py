def increase(n):
    '''
    increase(1234)
    >>> 
    1
    12
    123
    1234
    '''
    if n < 10:
        print(n)
    else:
        increase(n // 10)
        print(n)

def decrease(n):
    '''
    decrease(1234)
    >>> 
    123
    12
    1
    '''
    if n < 10:
        return True
    else:
        print(n // 10)
        decrease(n // 10)

def g(n):
    increase(n)
    decrease(n)

g(12345)