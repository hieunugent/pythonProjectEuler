class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def travelland(i, j):
                nonlocal grid
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                    return
                grid[i][j] = '-1'
                travelland(i-1, j)
                travelland(i, j-1)
                travelland(i+1, j)
                travelland(i, j+1)
        count = 0
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        travelland(i, j)
                        count += 1
        return count
def isSafe(i, j , visitted, grid):
    return (i>= 0 and j < len(visitted) and j >= 0 and j < len(visitted[0]) and not visitted[i][j] and grid[i][j])
def DFS( i, j , visitted, grid):
    rowDirec=[-1,-1,-1, 0, 0, 1, 1, 1]
    colDirec=[-1, 0, 1,-1, 1,-1, 0, 1] 
    visitted[i][j]= True
    for k in range(8):
        if isSafe(i+rowDirec[k], j +colDirec, visitted, grid):
            DFS(i+rowDirec[k], j + colDirec, visitted, grid)
  