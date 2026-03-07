
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

dicts ={"one":1,"two":2}
dicts["two"] ="Two"
dicts["three"] =3
print(dicts)
print(dicts["one"])



def traverseDict(dict):
    for key in dict:
        print(key,dict[key])

def searchValue(dict,value):
    for key in dict:
        if dict[key] ==value:
            return key,value
    return "Value not found"
print(searchValue(dicts,"3"))
traverseDict(dicts)

newDicts ={}.fromkeys([1,2,"hh"],7)
print(newDicts)


squares = {x:x*x for x in range(5)}
print(squares)
