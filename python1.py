'''Date : 12/01/2022 Name : K Prasad Achari'''
'''Given an array arr[ ] of N elements, your task is to 
find the minimum number of increment operations required to make all the elements of the array unique.
 ie- no value in the array should occur more than once. 
 In an operation a value can be incremented by 1 only.'''

def minIncrements(arr): 
    l=set()
    a=0
    for i in arr:
        while i in l:
            i += 1
            a += 1
        l.add(i)
    return a

arr=list(map(int,input().split(",")))
print(minIncrements(arr))

'''Input: 
arr = [1, 1, 2, 3]
Output:
3'''