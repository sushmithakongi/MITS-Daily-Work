'''Date:11/01/2023 Name:K Prasad Achari'''
'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while(l<r):
            if nums[i]+nums[l]+nums[r]==0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
            elif nums[i]+nums[l]+nums[r]>0:
                r-=1
            else:
                l+=1
    return res

nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))

'''input:nums=[-1,0,1,2,-1,-4]
output:[[-1,-1,2],[-1,0,1]]'''
        