
def threeSum(nums):
    l=len(nums)
    ans=set()
    k=0
    for i in range(l):
        dic={}
        for j in range(i+1,l):
            if k-nums[j]-nums[i] in dic:
                ans.add(tuple(sorted((nums[i],nums[j],k-nums[j]-nums[i]))))
            dic[nums[j]]=j
            #print(dic)
    return ans
print(threeSum([-1,0,1,2,-1,-4]))
                
                    

            
                
            
        