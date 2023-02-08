def findTargetSumWays(nums, target):
    dic={}
    l=len(nums)
    def helper(ind,res):
        if ind==l:
            return 1 if res==target else 0
        if (ind,res) in dic:
            return dic[(ind,res)]
        dic[(ind,res)]=(helper(ind+1,res+nums[ind]))+(helper(ind+1,res-nums[ind]))
        return dic[(ind,res)]
    return helper(0,0)
print(findTargetSumWays([1,1,1,1,1],3))
