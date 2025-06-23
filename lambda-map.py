# lambda functions - anonymous function, one line function

# def sums(a,b):
#     return a+b
   # lambda parameters: return
   # lambda parameters: 
   
sums= lambda a,b:a+b 
print(sums(23,45))


# oddEven=lambda a: "Even" if a%2==0 else "Odd"
oddEven=lambda a: print("Even") if a%2==0 else print("Odd")
oddEven(2)


print("-----------------")
# map
def listP(a):
    return a+20

# a=map(listP,[34,12,13,16,10,20])
a=map(lambda a:a+20,[34,12,13,16,10,20])
print(a)
print(list(a))

b=map(lambda a,b:a+b,[1,2,3,4],[11,12,13,14,15])
print(tuple(b))


# filter 
print("---------------------")
def filterMarks(a):
    mark=34
    if a>mark:
        return True

marks= filter(filterMarks,[35,36,56,44,23,12,32,28,89])
print(tuple(marks))


def filterVowels(a):
    vowels='aeiouAEIOU'
    if a in vowels:
        return True

fil= filter(filterVowels,"Gurminder Singh")
print(list(fil))


import random

print(random.randint(1,35))
print(random.randint(1,35))
print(random.randint(1,35))

li=['pink','yellow','green','orange','purple','blue','red','black','white']
print(random.choice(li))
print(random.choice(li))
print(random.choice(li))
print(random.choices(li,k=2))