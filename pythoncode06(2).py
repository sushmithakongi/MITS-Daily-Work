'''Date : 06/02/2023 Name : K Prasad Achari'''

'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].'''

def searchRange(nums, target):
    l=[]
    if target not in nums:
        res=[-1,-1]
        return res
    else:
        for i in range(0,len(nums)):
            if nums[i]==target:
                l.append(i)
        return [l[0],l[-1]]

nums=list(map(int,input().split(",")))
target=int(input())
print(searchRange(nums, target))

'''Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]'''
'''Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''




