'''Date:19/01/2023 Name: K Prasad Achari'''
'''Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.'''

def topKFrequent(nums,k):
    d={}
    for i in nums:
        d[i] = d.get(i,0) + 1
    #print(d)
    e={}
    for i,j in d.items():
        if j in e:
            e[j].append(i)
        else:
            e[j]=[i]
    #print(e)
    l=[[i,j] for i,j in e.items()]
    l.sort(key=lambda x:x[0],reverse=True)
    #print(l)
    ans=[]
    c=0
    for i,j in l:
        for x in j:
            c+=1
            ans.append(x)
            if c==k:
                return ans

nums=list(map(int,input().split(",")))
k=int(input())
print(topKFrequent(nums,k))

'''Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]'''

'''Input: nums = [1], k = 1
Output: [1]'''