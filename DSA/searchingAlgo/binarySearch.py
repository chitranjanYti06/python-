## value must be shorted in the binary search 
## them we can procede for the binary search
 
## 0   1  2  3  4  5  6  7  8  9
## 35 40 29 18 90 87 62 53 61 59 

# sort
# 0  1   2  3   4  5  6   7   8   9
# 18 29 35 40  53 59 61  62  87  90

#firstly we have to find the middle element
# m = l + u /2 
# if  item == list1[m]
#    return m
# if item < list1[m]  them we will get this item in the left half

# again apply binary serch in left half
# if binarySearch(list , 0 ,3)
# else:
# binarySearch(lsit ,5 ,9)

## time complexity of binary search is (log n)

def binarySearch(lst,key):
    start =0
    end=len(lst)-1

    while(start<=end):

        mid=(start + end) //2
        #start the comparison
        if(key== lst[mid]):
            return mid
        if(key < lst[mid]):
            end= mid-1
        
            # search in the left
        else:
            start=mid+1
    return None

print(binarySearch([10, 20, 30, 40, 50, 60, 70, 80 ,90],100))            
