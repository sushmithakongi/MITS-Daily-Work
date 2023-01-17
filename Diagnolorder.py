"""Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]"""
def findDiagonalOrder(mat):
        if not mat:
            return 0
        n=len(mat)+len(mat[0])-1
        res=[[] for i in range(0,n)]
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                res[i+j].append(mat[i][j])
        result=res[0]
        for i in range(1,len(res)):
            if i%2==1:
                result.extend(res[i])
            else:
                result.extend(res[i][::-1])
        return result
mat = [[1,2,3],[4,5,6],[7,8,9]]
l=findDiagonalOrder(mat)
print(l)