'''Date:25/01/2023 Name:K Prasad Achari'''

'''Given an m x n matrix, return all elements of the matrix in spiral order.'''

def spiralOrder(matrix):
    l=[[[]]*i for i in range(1,len(matrix)+1)]+[[]]
    ans=[]
    while 1:
        #top
        ans.extend(matrix.pop(0))
        if matrix in l:
            break
        #right
        r=len(matrix)
        for i in range(r):
            ans.append(matrix[i].pop())
        if matrix in l:
            break
        #bottom
        ans.extend(matrix.pop()[::-1])
        if matrix in l:
            break
        #left
        r=len(matrix)
        for i in range(r-1,-1,-1):
            ans.append(matrix[i].pop(0))
        if matrix in l:
            break
    return ans
    

matrix=eval(input())
print(spiralOrder(matrix))

'''Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]'''

'''Input: 
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''