'''Date:20/01/2023 Name:K Prasad Achari'''

'''Given an integer array nums where every element appears three times except for one, which appears exactly once.
 Find the single element and return it.'''

def singleNumber(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    #print(d)
    for i,j in enumerate(d):
        if d[j]==1:
            return j

nums=list(map(int,input().split(",")))
print(singleNumber(nums))

'''Input: nums = [2,2,3,2]
Output: 3'''

'''Input: nums = [0,1,0,1,0,1,99]
Output: 99'''
        