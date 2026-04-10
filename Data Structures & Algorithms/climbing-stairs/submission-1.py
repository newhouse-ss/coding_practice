class Solution:
    def climbStairs(self, n: int) -> int:
        # dp-function: dp(i) means the num of distinct ways up to and including i-th staircase.
        # recurrence: dp(i) = dp(i-1) + dp(i-2)
        # base case: i == 1 or i == 0.
        memo = {}
        def dp(i):
            if i == 1 or i == 0:
                return 1
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        return dp(n)