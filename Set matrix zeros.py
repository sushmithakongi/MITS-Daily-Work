"""Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]"""
def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=[]
    col=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row.append(i)
                col.append(j)
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j]=0
    return matrix
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
mat=setZeroes(matrix)
print(mat)