'''Date : 12/01/2022 Name : K Prasad Achari'''
'''Given an array of N integers arr[] where each element represents the max length of the jump 
that can be made forward from that element. Find the minimum number of jumps to reach the end of the array
 (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.'''

def minJumps(arr, n):
    c=0
    m=0
    res=0
    for i in range(0,n):
        m=max(m,i+arr[i])
        if c<i:
            return -1
        if c==i and i!=n-1:
            c=m
            res+=1
    return res

n=int(input())
arr=list(map(int,input().split(",")))
print(minJumps(arr,n))


'''Input:
n = 11 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] 
Output: 3 '''
	    
        