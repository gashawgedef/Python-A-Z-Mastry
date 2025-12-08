# """
# File: lists.py
# Author: Gashaw Gedef
# Purpose: To be filled
# """
# """
# Lists have many methods 

# list.append(x)
# list.extend(iterable)
# list.insert(i,x)
# list.remove(x)
# list.pop()
# The list data type has some more methods. Here are all of the methods of list objects:

# list.append(x)
# Add an item to the end of the list. Similar to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

# list.clear()
# Remove all items from the list. Similar to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index of the first occurrence of x in the list. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Similar to a[:].
# """


# families=["Fikir","Gashaw","Getachew","Alemwork","Yeshimebet","Gebremariam","Habtamu","Gebremariam","Andebet","Abrham","Liknesh"]

# print(families.count("Gashaw"),families.index("Gebremariam"))
# print(families.index('Gebremariam',6))
# print(len(families))
# families.reverse()
# families.append("Gedef")
# families.append("Meseret")
# for i  in families:
#     print(i)
# print("$$$$$$$$$$$$$$$$$$$ After Sorted#################")
# families.sort()
# copy_families =families.copy()# holding shallew copy of items
# for item in families:
#     print(item)

# print(families.pop(2))





# for item in copy_families:
#     print(item)

# """Using list as stack"""
# stack =[3,4,5]
# stack.append(6)
# stack.pop()
# stack.pop()
# for i in stack:
#     print(i)


# squares =[x**2 for x in range(10)]
# squares1 = list(map(lambda x: x**2, range(10)))

# for square in squares:
#     print(square)

# list1= [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(list1)

# combs=[]
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x!=y:
#             combs.append((x,y))
# print(combs)
