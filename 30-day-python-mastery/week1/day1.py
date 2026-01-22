
from collections import deque
import bisect

lst =[1,2,3]
dct = {1:'a'}
st =set([1,2])
tpl = (1,2)


squares =[x**2 for x in range(10)]
print(squares)

sorted_lst = sorted(squares,key=lambda x:-x)
print(sorted_lst)

bisect.insort(lst,4)

print(lst)


class Stack:
    def __init__(self):
        self.d =deque()
    def push(self,value):
        self.d.append(value)
    def pop(self):
        return self.d.pop()
    
class  Queue:
    def __init__(self):
        self.d = deque()
    def enqueue(self,value):
        self.d.append(value)
    def dequeue(self):
        return self.d.popleft()

# LeetCode placeholders (e.g., two sum, etc.)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# Practice: 5 problems similar
if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))  # [0,1]