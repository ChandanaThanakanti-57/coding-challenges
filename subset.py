def subset(nums,s,i):
    if i==len(nums):
        print(s)
        return
    subset(nums,s,i+1)
    s.append(nums[i])
    subset(nums,s,i+1)
    s.pop()
subset([1,2,3],[],0)
