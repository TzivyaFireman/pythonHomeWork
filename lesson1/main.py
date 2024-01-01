from datetime import datetime
from functools import wraps


#ex1:
def time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        print (end-start)
    return wrapper

@time
def func():
    for i in range(100000):
        print(i)


#ex2:

cache = {}

def MyCache(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        if args[0] in cache:
            return cache[args[0]]
        else:
            result = func(*args, **kwargs)
            cache.update({args[0]:result})
            print(result)
            return result
    return wraper


@MyCache
def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


def fib2(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


if __name__ == '__main__':
    func()
    fib(10)
    fib(15)
    fib(10)
    fib2(10000)
    fib2(40000)
    print(cache)