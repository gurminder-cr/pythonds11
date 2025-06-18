# Sets  - {}, heterogenous, unique elements, unordered 

set1={23,45,True,'hi','surbhi',45,6.78,100}
print(set1)

print("--------after add")
set1.add(33)
print(set1)

print("--------after update")
# set1.update({38,99,88})
set1.update([38,99,88])
print(set1)

print("----------after pop")
set1.pop()
print(set1)
set1.pop()
print(set1)

set1.remove(100)  # raise error if value is not present
print(set1)

set1.discard(122) #does not raise error if value is not present
print(set1)