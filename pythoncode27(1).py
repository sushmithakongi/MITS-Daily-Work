'''Date : 27/01/2023 Name : K Prasad Achari'''

'''Given an array of integers and another number. 
Find all the unique quadruple from the given array that sums up to the given number.'''

import itertools
def fourSum(arr, k):
    l=[]
    l1=[]
    for i in itertools.combinations(arr,4):
        if sum(i)==k:
            l.append(sorted(i))
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

arr=list(map(int,input().split(",")))
k=int(input())
print(*fourSum(arr, k))

'''Input:
a = [0,0,2,1,1]
K = 3
Output: 0 0 1 2 '''

'''Input:
a = [10,2,3,4,5,7,8]
k = 23
Output: 2 3 8 10 2 4 7 10 3 5 7 8 '''