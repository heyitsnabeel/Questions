target = 2
lst = [2,4,7,9,10,50,60]
low=0
high=len(lst)-1

# print(length)

def Binary_Search(lst,low,high):
    while low<=high:
        mid = (low+high)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]>target:
            high = mid-1
        elif lst[mid]<target:
            low = mid+1

    return -1        

out = Binary_Search(lst,low,high)
if out==-1:
    print("not in list")    
else:
    print(f"The index of target element is {out}")