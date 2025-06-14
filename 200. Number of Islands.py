class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #using bfs approach
        from collections import deque

        if not grid or not grid[0]:
            return

        visited = set()
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        island_count = 0

        q = deque([])

        def bfs():
            
            while q:
                i,j = q.popleft()
                for m,n in directions:
                    if 0 <= i+m < len(grid) and 0 <= j+n < len(grid[0]) and (i+m, j+n) not in visited and grid[i+m][j+n] == '1':
                        visited.add((i+m,j+n))
                        q.append((i+m,j+n))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #Zeros are automatically ignored
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i, j))
                    q.append((i,j))
                    bfs()
                    island_count += 1
               
        return island_count
            
