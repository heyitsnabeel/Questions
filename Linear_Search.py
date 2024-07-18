target = 9
lst = [2,4,7,9,10,50,78,60]

def Linear_Search(lst):
    for i in range(len(lst)):
        if(lst[i]==target):
            return i

out = Linear_Search(lst)
if out:
    print(f"The index of target element is {out}")
else:
    print("not in list")    