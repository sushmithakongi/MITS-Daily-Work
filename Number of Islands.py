"""Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3"""
def numIslands(grid):
        if not grid:
            return 0
        def dfs(i,j,visited):
            directions=[(0,1),(-1,0),(1,0),(0,-1)]
            stack=[]
            stack.append((i,j))
            visited.add((i,j))
            while stack:
                r,c=stack.pop()
                for dr,dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and (r+dr,c+dc) not in visited and grid[r+dr][c+dc]=="1":
                        visited.add((r+dr,c+dc))
                        stack.append((r+dr,c+dc))
            return 
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        islands=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j,visited)
                    islands=islands+1
        return islands
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a=numIslands(grid)
print(a)
                    