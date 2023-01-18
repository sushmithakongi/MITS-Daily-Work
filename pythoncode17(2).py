'''Date:17/01/2023 Name:K Prasad Achari'''
'''Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. 
Find whether element x is present in the matrix or not.'''

def search(n, m, matrix, x): 
    i=0
    j=m-1
    while (i<n and j>=0):
        if matrix[i][j]==x:
            return 1
        elif matrix[i][j]<x:
            i+=1
        elif matrix[i][j]>x:
            j-=1
    return 0

n=int(input())
m=int(input())
matrix=eval(input())
x=int(input())
print(search(n,m,matrix,x))

'''Input:
n = 3, m = 3, x = 62
matrix = [[3, 30, 38],[36, 43, 60],[40, 51, 69]]
Output: 0'''

''''Input:
n = 3, m = 3, x = 33
matrix = [[3, 33, 42],[16, 23, 60],[20, 31, 49]]
Output: 1'''
