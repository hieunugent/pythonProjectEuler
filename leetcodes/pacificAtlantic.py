# list of grid that can flow both side of matrix
# side one top left, side 2 bottom right
# algorithm 
# if the input is empty, immediately return an empty array
# initiallize variable that we will use to solve the problem
# number of rows and columns in our matrix
# 2 queues, one for the atlantic ocean, and one for the pacific ocean that will be used for BFS
# 2 data structures , again one for each ocean that we keep track of cell we already visited, to avoid infinite loop
# a small array that show direction will help with BFS
# figure out all the cells that are adjacent to each ocean, and fill the respective data structures with them 
# Perform BFS from each ocean. The data structure used to keep track of cells already visited has a double purpose - it also contains every cell that can flow into that ocean.
# Find the intersection, that is all cells that can flow into both oceans.
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i,0))
            atlantic_queue.append((i, num_cols-1))
            
        for i in range(num_cols):
            pacific_queue.append((0,i))
            atlantic_queue.append((num_rows-1, i))
            
        def bfs(queue):
            reachable= set()
            while queue:
                (row,col) = queue.popleft()
                reachable.add((row, col))
                for (x,y) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_row, new_col  = row+x, col+y
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    queue.append((new_row, new_col))
            return reachable
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pacific_reachable.intersection(atlantic_reachable))