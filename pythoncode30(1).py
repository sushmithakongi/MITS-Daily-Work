'''Date : 30/01/2023 Name : K Prasad Achari'''

'''Given an integer array nums, return the number of triplets chosen from the array that can make triangles 
if we take them as side lengths of a triangle.'''

def triangleNumber(nums):
    nums.sort()
    n=len(nums)
    ans=0
    for k in range(2,n):
        i=0
        j=k-1
        while i<j:
            if (nums[i]+nums[j])>nums[k]:
                ans += j-i
                j -= 1
            else:
                i += 1
    return ans

nums=list(map(int,input().split(",")))
print(triangleNumber(nums))

'''Input: nums = [2,2,3,4]
Output: 3'''

'''Input: nums = [4,2,3,4]
Output: 4'''