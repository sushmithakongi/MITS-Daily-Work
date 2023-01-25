'''Date : 24/01/2023 Name : K Prasad Achari'''

'''Given an array with N distinct elements, convert the given array to a reduced form where all elements are in range from 0 to N-1. 
The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, 
and N-1 is placed for the largest element.'''

def convert(arr, n):
    a = sorted(arr)
    d = {}
    for i in range(n):
        d[a[i]]=i
    for i in range(n):
        arr[i] = d[arr[i]]
    return arr

n=int(input())
arr=list(map(int,input().split(",")))
print(*convert(arr, n))

'''Input:
n = 3
arr = [10, 40, 20]
Output: 0 2 1'''

'''Input:
n = 5
arr = {5, 10, 40, 30, 20}
Output: 0 1 4 3 2'''