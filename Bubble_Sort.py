lst = [6,7,2,9,4,1,20,10]
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)        
