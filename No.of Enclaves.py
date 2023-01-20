"""Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary."""
def numEnclaves(grid):
        visited = set()
        
        count = 0
        
        def dfs(i,j):
            
            if (i,j) in visited or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            visited.add((i,j))
            grid[i][j] = "#"
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1 and grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count +=1
        
        return count
grid =[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
a=numEnclaves(grid)
print(a)