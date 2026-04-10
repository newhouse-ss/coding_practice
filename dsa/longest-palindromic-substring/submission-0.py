class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Let's define the dp-function: dp(i, j) means 
        # whether s[i:j] is a parlindrome.
        # recurrence: dp(i, j) = (s[i] == s[j]) and dp(i+1, j-1)
        # base case: if i == j: odd, return s[i]
        # if i > j: return ''
        memo = {}
        def dp(i, j):
            if i == j:
                return True
            if i > j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = (s[i] == s[j]) and dp(i+1, j-1)
            return memo[(i, j)]

        n = len(s)
        for length in range(n, 0, -1):
            for i in range(n-length+1):
                if dp(i, i + length-1):
                    return s[i:i+length]
