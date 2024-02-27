# sum from 1 to 10
# 1+2+3+...............10
# sum=0
# for i in range(1 , 11):
#     sum=sum+i#sum+=i
# print(sum) 

# Ask user for the sum
n=int(input("Enter the number: "))
total = 0
for i in range(1,n+1):
    total+=i
print(total)    