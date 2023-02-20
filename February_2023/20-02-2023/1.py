def searchInsert(nums,target):
    i=1
    if target in nums:
        return nums.index(target)
    else:
        while i<=target:
            temp1=target-i
            temp2=target+i
            if (temp1 in nums):
                return nums.index(temp1)+1
            elif (temp2 in nums):
                return nums.index(temp2)-1
        i+=1

print(searchInsert([1,3,5,6],5))#2
print(searchInsert([1,3,5,6],2))#1
print(searchInsert([1,3,5,6],7))#4

'''Given a sorted array of distinct integers and a target value,
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.'''