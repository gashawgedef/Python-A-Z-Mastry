
"""Dunder or Magic methods"""

"""__init__() method"""
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x!r},{self.y!r})"
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    """Equality Comparison"""
    def __eq__(self, value):
        if not isinstance(value,Point):
            return NotImplemented
        return (self.x,self.y)==(value.x,value.y)
    
p = Point(-3,2)
p1 =Point(5,5)
p2 = Point(5,5)
# print(p)
print(repr(p))
print(str(p))
print(p.x, p.y)
print(p1 ==(5,5))