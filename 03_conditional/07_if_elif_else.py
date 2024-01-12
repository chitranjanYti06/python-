# if elif els statement

# show ticket pricing

# 0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# if we want check the multiple statement then we use if elif and else statement

user_age = int(input("Enter user age\t"))

if(user_age <= 3):
    print("Ticket Price : free")
elif(4 <user_age <= 10):
    print("Ticket price : 150")   
elif(user_age <= 60):
    print("Ticket price : 250")   
else:
    print("Ticket price : 200")   
