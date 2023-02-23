class Solution:
    def maximumCount(self, nums):
        negativeCount=0
        positiveCount=0
        for num in nums:
            if num<0:
                negativeCount+=1
            elif num>0:
                positiveCount+=1
        if negativeCount>positiveCount:
            return negativeCount
        else:
            return positiveCount

S=Solution()
nums=list(map(int,input().split(" ")))
print(S.maximumCount(nums))
