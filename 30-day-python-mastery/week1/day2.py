
from  functools import partial,wraps

def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

print(func(1, "Gashaw", a=2))

partial_func = partial(func, 1, a=2)

def higher_order(f):
    def wrapper(*args):
        return f(*args) + 1
    return wrapper
# Build reusable utility module (export to utils/ later)
# In this script: example
if __name__ == "__main__":
    func(1,2, a=3)
