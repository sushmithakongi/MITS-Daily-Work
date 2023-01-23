def arrayChange(nums, operations):
    dic={}
    for i in range(len(nums)):
        dic[nums[i]]=i
    for opr in operations:
        ind=dic[opr[0]]
        nums[ind]=opr[1]
        dic[opr[1]]=ind
    return nums
print(arrayChange([1,2,4,6],[[1,3],[4,7],[6,1]]))
