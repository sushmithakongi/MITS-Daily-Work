#You are given a sorted array consisting of only 
#integers where every element appears exactly twice, 
#except for one element which appears exactly once.
'''
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

 '''

class Solution:
    def singleNonDuplicate(self, nums):
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        for k,v in d.items():
            if v == 1:
                return k
            
S=Solution()
print(S.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(S.singleNonDuplicate([3,3,7,7,10,11,11]))