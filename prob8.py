"""Given a square matrix, turn it by 90 degrees in an anti-clockwise direction without using any extra space
Examples: 
Input:
Matrix:        1  2  3
               4  5  6
               7  8  9
Output:        3  6  9 
               2  5  8 
               1  4  7 """
def rotateMatrix(mat):
    for i in range(len(mat)):
        mat[i].reverse()
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()
mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
rotateMatrix(mat)
displayMatrix(mat)