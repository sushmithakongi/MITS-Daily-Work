'''Date:11/01/2023 Name:K Prasad Achari'''
'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.'''
def majorityElement(nums):
    d=dict()
    k=len(nums)//3
    a=[]
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in nums:
        if d[i]>k and i not in a:
            a.append(i)
    return a

nums=[3,1,2,3,3]
print(majorityElement(nums))

'''input:nums=[3,1,2,3,3]
output:[3]'''
