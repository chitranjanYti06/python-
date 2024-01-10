## time complexity will be o(n)
## because we have to do n compariosn in the liner search
def linerSearch(lst,key):
    for i in range(0,len(lst)-1):
        if(key == lst[i]):
            return i
    return None
print(linerSearch([4,8,8,9,5,10,53,8,9],10))    