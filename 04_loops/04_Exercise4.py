# problem
# ask user to input a number containing more than one digit
# example = 1256
# calculate 1+2+5+6


# algorithem -(method to solve problem in human language)
# ask input in string ,i.e don't change string to int
# example - "1256"
# pick string character one by one and change to int 
# int(example[0]) + int(example[1]) .... go upto len(example)

# 
i=0
sum = 0
number = input("Enter a number")
while(i < len(number)):
    sum= sum +int( number[i])
    i+=1
print(sum)    

