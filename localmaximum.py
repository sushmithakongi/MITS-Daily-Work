def largestLocal(grid):
    n=len(grid)
    newMatrix=[[0]*(n-2) for _ in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            curmax=0
            for start in range(3):
                for end in range(3):
                    curmax=max(curmax,grid[start+i][end+j])
            newMatrix[i][j]=curmax
                #print(newMatrix)
    return newMatrix
print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
                
