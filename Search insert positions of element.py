"""
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]"""
def searchRange(nums,target):
    if target not in nums:
        return [-1,-1]
    output=[]
    i=0
    while i<=len(nums)-1:
        if nums[i]==target:
            output.append(i)
        i=i+1
    return [output[0],output[len(output)-1]]
nums = [5,7,7,8,8,10]
target = 0
searchRange(nums,target)