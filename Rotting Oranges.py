"""Rotting Oranges
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally."""
def orangesRotting(grid):
        q=list()
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        time=0
        while q and fresh>0:
            for x in range(len(q)):
                a,b=q.pop(0)
                for i,j in [[a-1,b],[a+1,b],[a,b+1],[a,b-1]]:
                    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                        continue
                    grid[i][j]=2
                    q.append([i,j])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
grid = [[2,1,1],[1,1,0],[0,1,1]]
a=orangesRotting(grid)
print(a)