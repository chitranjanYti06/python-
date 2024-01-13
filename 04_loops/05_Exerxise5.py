# ask a user for name
# Example - chitranjan Kumer
# print count of each words
# output :
  #   C : 1
  #   h : 1
  #   i : 1
  #   t : 1
  #   r : 1
  #   a : 3
  #   n : 1
  #   j : 1
  #   a : 1
  #   n : 1
  #     : 1
  #   k : 1
  #   u : 2
  #   m : 1
  #   a : 1
  #   r : 2
i=0
temp = ""
name = input("Enter your name")
while(i < len(name)):
    if name[i] not in temp:
            temp+= name[i]
            print( f" {name[i]} : {name.count(name[i])}")
    i+=1
