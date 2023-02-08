'''Given a sorted array arr[] of size N. Find the element that appears only once in the array. 
   All other elements appear exactly twice. 
Example 1:
Input:
N = 11
arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
Output: 4
Explanation: 4 is the only element that 
appears exactly once.'''

def findOnce(arr : list, n : int):
    d=dict()
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
             return i
arr=[1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
n=11
a=findOnce(arr,n)
print(a)