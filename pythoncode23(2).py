'''Date:23/01/2023 Name: K Prasad Achari'''
'''You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.'''

def findSubArrays(arr):
    lists = []
    for i in range(len(arr) + 1):
        for j in range(i):
            lists.append(arr[j: i])
    c=0
    for i in lists:
        if sum(i)==0:
            c=c+1
    return c

arr=list(map(int,input().split(",")))
print(findSubArrays(arr))

'''Input:
arr = [0,0,5,5,0,0]
Output: 6'''

'''Input:
arr = [6,-1,-3,4,-2,2,4,6,-12,-7]
Output: 4'''