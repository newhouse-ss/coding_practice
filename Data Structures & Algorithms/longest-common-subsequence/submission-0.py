class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP: 1. longest; 2. The current match will affect the final result.
        # dp-function: dp(i, j) means the LCS of text1[:i] and text2[:j]
        # recurrence: dp(i, j) = 1+dp(i-1, j-1) if text1[i] == text2[j]
        # dp(i, j) = max(dp(i-1, j), dp(i, j-1))
        # base case: if one of i, j if 0, return 0.
        memo = {}
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = dp(i-1, j-1)+1
            else:
                memo[(i, j)] = max(dp(i-1, j), dp(i, j-1))
            return memo[(i, j)]
        
        m, n = len(text1), len(text2)
        return dp(m-1, n-1)