# Exercise - Watch Coco

# Ask user's name and age
# if user's name start with 'a' or 'A' and age is above 10 then
# print 'you can watch coco movie'
# Else print 'sorry ,you cannot watch coco'

username= input("Enter username\t")
user_age= int(input("Enter user age\t"))

if (username[0]== 'a' or username[0] =='A') and user_age >10 :
    print("you can watch coco movie")
else:
    print("Sorry, you cannot watch coco")    
