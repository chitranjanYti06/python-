# take two comma seprated inputs from user
# 1.) user's name
# 2.) a single character


# output - 2 print lines
#  1.) user's name length
#  2.) count the character that user inputed (bonus : case insensitive count)

user_name,char = input("Enter the values\t").split(",")
print(len(user_name.strip()))
print((user_name.strip().lower()).count(char.strip().lower()))

# "  Chitanjan " ---------------> "Chitranjan" ------------> "chitranjan"
# " A "------------------------->"A" ----------------------"a"

# print((user_name.strip().lower()).count(char.strip().lower()))