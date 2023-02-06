"""Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands
Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2"""
def closedIsland(grid):
        def dfs(grid, i, j):
            if grid[i][j] == 1:
                return True
            if i<=0 or j<=0 or i>=len(grid)-1 or j>= len(grid[0])-1:
                return False
            
            grid[i][j] = 1
            
            t1 = dfs(grid,i+1,j)
            t2 = dfs(grid,i-1,j)
            t3 = dfs(grid,i,j+1)
            t4 = dfs(grid,i,j-1)
            
            return t1 and t2 and t3 and t4
        
        count = 0
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 0 and dfs(grid,i,j):
                    count += 1
        return count
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
a=closedIsland(grid)
print(a)
        
