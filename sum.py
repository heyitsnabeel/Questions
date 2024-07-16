nums = [3,3]
target = 6
lst = []

for i in range(len(nums)-1):
    for j in range(1,len(nums)):
        if (nums[i]+nums[j]==target):
            lst.extend([i,j])

print(lst)

# while(j<len(nums)):
#     if (nums[i]+nums[j]==target):
#         print(f"{i}, {j}")

#     j+=1
#     i+=1
