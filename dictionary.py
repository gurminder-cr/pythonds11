# dictionary -- {}, key:value

# a={}
# a=set()
# print(a)
# print(type(a))

# a.update({23,34})
# print(a)


dict={'name':'Pratham','classes':'btech', 'rollno':1234,23:'twentythree','isownapet':True}
print(dict)

dict.update(marks=34)
print(dict)
dict.update(classes='bca')
print(dict)

print(dict['name'])

dict['name']='Nakul'
dict['college']='SBSSU'
print(dict)

print("-----------------")

dict.pop('marks')
print(dict)

# dict.get()
# print(dict['colleges'])

print(dict.get('colleges','Value is not present'))


print("----------------")
print(dict.keys())
print(dict.values())
print(dict.items())


# for i in dict.values():
#     print(i)
for i,j in dict.items():
    print(i,"==",j)
    
    
    
print('---------------------------')
print('---------------------------')

d={
    'name':{
        'firstname':'Nakul',
        'lastname':'Dhiman'
    },
    'rollno':3456,
    'classes':'btech',
    'address':{
        'permanent':'Pathankot',
        'temp':'mohali'
    },
    'marks':[45,56,78,87]
}
print(d)
print(d['address'])
print(d['address']['temp'])
print(d['marks'][2])


print("---Enumerate function-------")
# enumerate function 

for i,j in enumerate(dict.items()):
    print(i,"---",j)
    
    
dict.clear()
print(dict)

