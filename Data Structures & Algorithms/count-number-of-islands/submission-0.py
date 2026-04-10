class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(row, col):
            # this will add all lands(nodes) in an island(component) into seen
            for dx, dy in directions:
                nr, nc = row+dx, col+dy
                if nr in range(m) and nc in range(n) and (nr, nc) not in seen and grid[nr][nc] == '1':
                    seen.add((nr, nc))
                    dfs(nr, nc)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    count += 1
                    dfs(i, j)

        return count