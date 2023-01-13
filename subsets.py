def subsets(nums):
    res=[]
    n=len(nums)
    for i in range(2**n):
        res.append([])
        for j in range(n):
            if (i&(1<<j))>0:
                res[i].append(nums[j])
    return res
print(subsets([1,2,3]))
