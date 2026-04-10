class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The idea comes from 2 steps: dp to judge whether a parlindrome;
        # enumerate to find the longest one.
        # dp-function: dp(i, j) means whether s[i:j+1] is a parlindrome.
        # recurrence: dp(i, j) = (s[i] == s[j]) and dp(i+1, j-1)
        # base case: i == j or i > j-->True
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
            for i in range(n - length + 1):
                if dp(i, i+length-1):
                    return s[i:i+length]
                    