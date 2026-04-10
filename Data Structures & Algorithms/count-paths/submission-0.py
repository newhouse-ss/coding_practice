class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The main idea on matrix DP is very intuitive, the current state comes from certain directions.
        # dp-function: dp(i, j) means the unique paths to reach (i, j) block.
        # recurrence: dp(i, j) = dp(i-1, j) + dp(i, j-1)
        # base case: start and edges.
        memo = {}
        def dp(i, j):
            if (i, j) == (0, 0):
                return 1
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dp(i-1, j) + dp(i, j-1)
            return memo[(i, j)]
        
        return dp(m-1, n-1)