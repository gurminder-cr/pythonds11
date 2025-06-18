# tuple - (), heterogneous, ordered(indexed), immutable(cannot change)

a=(12,34,'hello',True,9.9)
print(a)
print(type(a))

l=[12]
print(type(l))
k=(12,)
print(type(k))

print(a)
# slicing 
print(a[3])
print(a[:])  # start stop step
print(a[:4])  # start stop step
print(a[:4:2])  # start stop step
print(a[::-1])
# (12, 34, 'hello', True, 9.9)
# a[2]=56
# print(a)

print(a)
a=list(a)
print(a)
a[2]=56
a=tuple(a)
print(a)

print(a.index(56))
print(a.count(True))