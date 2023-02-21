#Given an array of positive integers nums,
#return the maximum possible sum of an ascending subarray in nums.

class Solution:
    def maxAscendingSum(self, nums):
        n = len(nums)
        m = a = nums[ 0 ]
        for i in range( 1, n ):
            if nums[ i ] > nums[ i - 1] :
                a += nums[  i ]
            else:
                a = nums[ i ]
            m = max( m, a )        
        return m 

S=Solution()
nums=[10,20,30,5,10,50]
print(S.maxAscendingSum(nums))
