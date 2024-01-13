# exercise one of three
# sum of n natural numbers
# ask a user for natural number(n)
#  print total from 1 to n

natural_number= int(input("Enter a natural number to sum  "))
i=1
sum =0
while(i<= natural_number):
    sum += i
    i+=1
print(sum)  

print((natural_number*(natural_number+ 1))/2)