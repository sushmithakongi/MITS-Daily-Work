#Go program to read an array and counts the positive and negative
#numbers and prints the maximum count
#Input:[1,2,3,0,0,-1,-2,-3,-4]
#Output:4


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
nums=list(map(int,input().split(",")))
print(S.maximumCount(nums))
