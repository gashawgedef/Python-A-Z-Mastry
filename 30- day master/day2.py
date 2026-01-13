
import sys

# x  = [1,2,3]
# y = x
# z = [x,"other"]


# print(id(x))
# print(id(y))
# # print(id(z))

# print(sys.getrefcount(x))

class Transaction:
    def __init__(self, amount):
        self.amount = amount

txn = Transaction(1000)
print(sys.getrefcount(txn))  # ~2

cache = [txn]  # +1
print(sys.getrefcount(txn))  # ~3

del cache  # -1
print(sys.getrefcount(txn)) 