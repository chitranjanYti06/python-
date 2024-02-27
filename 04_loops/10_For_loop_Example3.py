# practice for loop
# ask user name and count each character
#  "chitranjan kumar"

# c: 1
# h: 1
# i: 1
# t: 1
# r: 2
# a: 3
# n: 2
# j: 1
#  : 1
# k: 1
# u: 1
# m: 1

name=input("Enter your name:")
temp =""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp+=name[i]