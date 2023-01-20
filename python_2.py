'''Date:13/01/2023 Name:K Prasad Achari'''

'''Given 2 sorted arrays Ar1 and Ar2 of size N each. Merge the given arrays and 
find the sum of the two middle elements of the merged array.'''

def findMidSum(ar1, ar2):
    for i in ar1:
        ar2.append(i)
    ar2.sort()
    mid = len(ar2)//2
    return ar2[mid-1]+ar2[mid]
    
	
    

ar1=list(map(int,input().split(",")))
ar2=list(map(int,input().split(",")))
print(findMidSum(ar1,ar2))

'''Input:
ar1 = {1, 2, 4, 6, 10}
ar2 = {4, 5, 6, 9, 12}
Output: 11'''