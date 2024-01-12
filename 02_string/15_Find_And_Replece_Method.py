# replace() method
# find() nethod

string ="she is beautiful and she is good dancer"
print(string.replace("is","was",1))# we can also give that how many character will be replace in third parameter conversion
# will be done starting

# if we want to know the position of any character in the string so we can

# print(string.find("is",1)) # is find method we can also give the positon from where we have to start the searching

is_position_one= string.find("is") # is pos1 --- number
is_position_two =string.find("is",is_position_one+1)
print(is_position_two)
