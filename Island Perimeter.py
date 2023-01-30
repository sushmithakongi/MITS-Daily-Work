"""Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:
Input: grid = [[1]]
Output: 4
Example 3:
Input: grid = [[1,0]]
Output: 4"""
def islandPerimeter(grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):    
			# If already visited return 0
            if (r, c) in visited:
                return 0
			# If out of bound or encountered water return 1
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 1
            visited.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
a=islandPerimeter(grid)
print(a)