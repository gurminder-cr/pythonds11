# a=10
# b=20
# print("a is",a,"b is",b)

# # formatted strings
# print(f"a is {a} and b is {b}")


# Main function  


def sumAll():
    print("All sums")
    
def sumRet(**a):
    print(a)
    sum=0
    for i in a.values():
        sum+=i
    return sum
def sumRet(*a):
    print(a)
    sum=0
    for i in a:
        sum+=i
    return sum

# sumRet(23,45,67,89)
# sumAll()

# if __name__=="__main__":
#     sumAll()
#     sumRet()


# a=int(input("Enter a "))
# b=int(input("Enter b "))

# # print(a/b)
# try:
#     print(a/b)
    
# # except Exception as e:
# #     print(e)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("Always executed")
# print("Hello After division")



li=[34,32,12,31]
# print(li[4])

try: print(li[4])
except Exception as e: print("Error is",e)
