'''Date : 30/01/2023 Name : K Prasad Achari'''

'''Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j])'''

def findPairs(nums, k):
    count = 0
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i] - nums[j] == k or nums[j] - nums[i] == k:
                count += 1
    return count

nums=list(map(int,input().split(",")))
k=int(input())
print(findPairs(nums,k))

'''Input: nums = [1,2,3,4,5], k = 1
Output: 4'''
'''Input: nums = [1,3,1,5,4], k = 0
Output: 1'''
