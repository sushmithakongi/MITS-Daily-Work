
def sortColors(nums):   
    a,b,c=0,0,0
    for i in nums:
        if i==0:
            a+=1
        elif i==1:
            b+=1
        else:
            c+=1
    for i in range(a):
        nums[i]=0
    for i in range(b):
        nums[i+a]=1
    for i in range(c):
        nums[i+a+b]=2
    return nums
print(sortColors([2,0,1]))
        
        
        
