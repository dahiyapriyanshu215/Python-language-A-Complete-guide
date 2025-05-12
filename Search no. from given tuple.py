nums = [1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
print("Number to be found is:",x)
for i in nums:
    if(i==x):
        print("found at index:", idx)
    else:
        print("finding...")
    i=i+1
    idx = idx + 1