'''Date : 24/01/2023 Name : K Prasad Achari'''

'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.'''

def findDuplicates(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=[]
    for i,j in d.items():
        if j>=2:
            ans.append(i)
    return ans

nums=list(map(int,input().split(",")))
print(findDuplicates(nums))

'''Input: 
nums = [4,3,2,7,8,2,3,1]
Output: [3,2]'''

'''Input: nums = [1,1,2]
Output: [1]'''