# Heterogenous data storage, [], mutable(can change), index based value

l=['hello',34,5.6,True,23,67,9.9]
print(l)
print(type(l))

# access
print(l[5])
# print(l[7])
print(len(l))

# slicing 
print("-----")
# ['hello', 34, 5.6, True, 23, 67, 9.9]

# print(l)  #start,stop, step  [::]
print(l[:])
print(l[1:5])
print(l[:5])
print(l[2:])

print(l[1:6:1])
print(l[1:6:2])
print(l[::-1])
print(l[1:5:-1])


# functions and methods 
l1=[12,34,54,33,22,34,78]
print(l1)
l1.insert(2,44) #index, value
print(l1)

#update
l1[4]=100
print(l1)


l1.insert(4,[1,2,3])
print(l1)
print(l1[4][1])

l1.extend([9,7,6])
print(l1)

l1.append([3,4,5])
print(l1)

print("------------------")
print("------------------")
n=[34,23,10,45,6,23,10]
print(n)
# n.sort()
# print(n)

n.remove(23)  #Remove first occurence of value,Raises ValueError if the value is not present.
print(n)

print("-------------")
# n.pop()
n.pop(2) # return error if index is not present
print(n)

# n.clear()
# print(n)

# append function
l2=[]

for i in n:
    # print(i)
    l2.append(i*2)


print(l2)
    