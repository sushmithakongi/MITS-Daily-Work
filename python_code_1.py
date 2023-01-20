'''Date:16/1/2023 Name:K Prasad Achari'''
'''Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.'''

def combinationSum(arr, target):
    def f(i,d,s):
        if s==target:
            ans.append(sorted(d))
        if i==n or s>=target:
            return
        f(i,d+[arr[i]],s+arr[i])
        f(i+1,d,s)
    n=len(arr)
    ans=[]
    f(0,[],0)
    return ans   

arr=list(map(int,input().split(",")))
target=int(input())
print(combinationSum(arr, target))

'''Input: arr = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]'''