# str1="Gurminder Singh"

# print(str1)

# # slicing
# print(len(str1))
# print(str1[:])  # start stop step : :
# print(str1[:7])
# print(str1[2:14])
# print(str1[2:])
# print(str1[::1])
# print(str1[::2])
# print(str1[::-1])
# print(str1[::-2])
# print(str1[1:10:-2])
# print(str1[10:1:-2])

# # methods
# print(str1.lower())
# print(str1.upper())
# print(str1.capitalize())
# print(str1.title())
# print(str1.swapcase())

# st="     hi    hello  "
# print(st.strip())
# print(st.lstrip())
# print(st.rstrip())

# print(str1.endswith("gh"))
# print(str1.startswith("Gu"))

# print(str1.find("m"))
# print(str1.find("min"))
# print(str1.count("m"))

# m="hello how are you"
# print(m.find("o",5))  #starts  5
# print(m.find("m"))  #Returns -1 if value is not exist

# print(m.index('m')) # returns value error if value not exists

print("------------")

a="Sourav kumar"
print(a)

print(a.replace('a','o')) # old string, new string
u="Hello how are you"

print(u.replace('o','are'))

# split
print(u.split())
print(u.split('o'))

l="234#mnsfbjs#fbsrb#brgb#mndfbgmndrbg#sfbf"
print(l.split('#'))

for i in u:
    print(i+"_")