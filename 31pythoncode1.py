def nextPermutation(nums):
    index=-1
    l=len(nums)
    for i in range(l-2,-1,-1):
        if(nums[i]<nums[i+1]):
            index=i
            break
    if(index>-1):
        for i in range(l-1,index,-1):
            if(nums[index]<nums[i]):
                nums[index],nums[i]=nums[i],nums[index]
                break
    left,right=index+1,l-1
    while(left<right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
a=[1,2,3]
nextPermutation(a)
print(a)