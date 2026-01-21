
# numbers = [1,2,3,4,5,6]

# result = []
# for n in numbers:
#     square = n**2
#     if square > 10:
#         result.append(square)

# result1 = [square1 for num in numbers if (square1:=num**2)>10]
# print(f"Walrus Operators have been completed{result1}")

# for i in result:
#     print(i)


class CountUp:
    def __init__(self,limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self
    def __next__(self):
        if self.current >=self.limit:
            raise StopIteration
        self.current+=1
        return self.current
    
for n in CountUp(3):
    print(n)
    

    