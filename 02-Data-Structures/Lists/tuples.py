tuples =1,2,3,4,5,6,"Gashaw"
print(tuples)
#tuples are imutable data structures
# dicts=dict([(1,2),(3,4)])
# print(dicts)
dicts ={x:x**2 for x in [1,2,3]}
print(dicts)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

"""Retrive the vale and index at the same time"""
families= ["Gashaw","Getachew","Alem","Sirash"]
for i, v in enumerate(families):
    print(i, v)
