
# names =["Mine","Gashaw","Gedef"]

# for item in range(len(names)):
#     names[item] = names[item]+ "+"
#     print(item)
#     print(names[item])


# print(names[-3 ])
# print("Gashaw" in names)
# for i in names:
#     print(i)  

empty =[]
empty.extend(["Alemwork","Gedef","Shibabaw"])
print(empty)
for i in empty:
    print(i)

"""Slice of delete from list"""


"""Finding Missing Number"""
def find_missing_number(arr):
    n = len(arr) + 1  # because 1 number is missing
    total = n * (n + 1) // 2
    return total - sum(arr)

myDict =dict()
print(myDict)

myDicts ={}
print(myDicts)