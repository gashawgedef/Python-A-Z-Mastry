

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def log(func):
    @wraps(func)
    def wrapper_log(*args,**kwargs):
        """Implementing Decorators"""
        print("Before Log Wrapper")
        print(f"Calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper_log

@log
def multiply(a,b,c):
    return a*b*c

@my_decorator
def add(a,b):
    return a+b



print(multiply(1,2,4))
print(multiply.__name__)

print(add(3,5))
print(add.__name__)