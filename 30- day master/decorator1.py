
# def my_decorator(fun):
#     def wrapper():
#         print("Before the Function")
#         fun()
#         print("After the function")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Gashaw Gedef")

# # decorated = my_decorator(say_hello)
# # decorated()
# print(my_decorator(say_hello()))


def my_decorator(fun):
    def wrapper(*args,**kwargs):
        print("Before")
        result = fun(*args,**kwargs)
        print("After")
        return result
                                                         
        
    return wrapper

@my_decorator
def add(a,b):
    return a+b


print(add(3,5))
print(add.__name__)