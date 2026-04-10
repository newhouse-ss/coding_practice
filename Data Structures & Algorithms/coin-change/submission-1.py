class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is a complete knapsack question.
        # dp-function dp(i, amount) means the the min num of coins
        # to sum an amount, where the coins come from [0, i]-th coins.
        # recurrence: dp(i, amount) = min(dp(i-1, amount), dp(i, amount-coins[i]))
        # base case: through i<0 and amount == 0
        memo = {}
        def dp(i, amount):
            if i >= 0 and amount == 0:
                return 0
            if i < 0:
                return float('inf') # -1 means we can't find a combination.
            if amount < 0: #pitfall
                return float('inf')
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            memo[(i, amount)] = min(dp(i-1, amount), dp(i, amount-coins[i]) + 1)
            return memo[(i, amount)]
        
        n = len(coins)
        return dp(n-1, amount) if dp(n-1, amount) != float('inf') else -1