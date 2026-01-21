
def greet():
    print(" Hello Gashaw Gedef")
say_hello =greet
say_hello()


def outer():
    def inner():
        print("Inner Function")
    return inner
fn=outer()
fn()

