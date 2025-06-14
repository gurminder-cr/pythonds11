#type casting 
a=12
print(a)
print(type(a))
print(float(a))
a= float(a)
print(type(a))

s=11.23
print(int(s))


i=True
print(int(i))

j=False
print(int(j))


k=12
print(bool(k))
l=0
print(bool(l))



# operators 
# --  Arithmetic operators: -- +,-,*,/,%,//
# n= int(input('enter n '))
# y= int(input('enter y '))

# print("The value of n is",n)
# print("The value of y is",y)
# print(n+y)
# print(n*y)
# print(n/y)
# print(n-y)
# print(n%y)
# print(n//y)


# Assignment =,+=,-=,*=,/=
a=10

a+=20 # a=a+20
a-=10 # a=a-10- 20
a*=20 # a=a*20  400
a/=10 # a=a/10 - 40
print(a)

# Relational ==,!=,>,<,>=,<= -- True, False 
print(12>40) 
print(33>33)
print(3<3)
print(3<=3)
print(3!=3)
print("------------------")
print("------------------")
# Logical operators  and, or, not
print(14>56 and 45>6) 
print(33<56 or 44>34)
print(33<56 or 44<34)

print( not 44>5)


# Membership - in not in 
print("------------")
naam="Gurminder Singh"
print("md" in naam)
print("mind" in naam)
print("mind" not in naam)



# Identity operator 
a=10
b=10
c='hi'
d='hi'
print(id(a))
print(id(b))
print(id(c))
print(id(d))

e=input("e ")
f=input("f ")
print(id(e))
print(id(f))

# identity operator 
print(a is b)
print(a is not b)

print(e is f)

print("added by surbhi")