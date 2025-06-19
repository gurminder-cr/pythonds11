# list comprehension 

# li=[]
# for i in range(20):
#     li.append(i)
# print(li)

# #  i for i in range() 
# l=[i for i in range(20)]
# print(l)



# for i in range(20):
#     if i%2==0:
#         print(i)
#  i for i in range() if i%2==0


# l=[i for i in range(20) if i%2==0]
# print(l)
l=[i if i%2==0 else i**2 for i in range(20)]
print(l)


l=[45,56,87,54,33,21,34,56,77,90]
a=[ i for i in l if i%3==0]
print(a)

# nested for loop in list comp
a=[1,2,3,4]
b=[5,6,7,3]

v=[i for i in a for j in b if i==j]
print(v)




l=[12,34,56,78]
k=[34,56,22,33,89]

print("-------zip------------")
# for i in zip(l,k):
#     print(i)
for i,j in zip(l,k):
    print(i,"--",j)
    