'''Date:19/01/2023 Name:K Prasad Achari'''

'''Given an array arr[] of size N and an integer K. 
Find the maximum for each and every contiguous subarray of size K.'''

def max_of_subarrays(arr,n,k):
    lis=[]
    for i in range(n+1):
        for j in range(i):
            lis.append(arr[j:i])
    res=[]
    for i in lis:
        if len(i)==k:
            res.append(max(i))
    return res

n=int(input())
k=int(input())
arr=list(map(int,input().split(" ")))
print(*max_of_subarrays(arr,n,k))

'''Input:
n = 9, k = 3
arr = [1 2 3 1 4 5 2 3 6]
Output: 
[3 3 4 5 5 5 6]'''

'''Input:
n = 10, k = 4
arr = [8 5 10 7 9 4 15 12 90 13]
Output: 
[10 10 10 15 15 90 90]'''