class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(row, col, reachable):
            reachable.add((row, col))
            for dx, dy in directions:
                nr, nc = row+dx, col+dy
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in reachable and heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, reachable)
        
        for i in range(m):
            dfs(i, 0, pacific)      # 左边界 → 太平洋
            dfs(i, n-1, atlantic)   # 右边界 → 大西洋
        for j in range(n):
            dfs(0, j, pacific)      # 上边界 → 太平洋
            dfs(m-1, j, atlantic)   # 下边界 → 大西洋
        
        return list(pacific & atlantic)