nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
print("Number to be found is:",x)
while i<len(nums):
    if(nums[i]==x):
        print("found at index:",i)
    else:
        print("finding...")
    i=i+1