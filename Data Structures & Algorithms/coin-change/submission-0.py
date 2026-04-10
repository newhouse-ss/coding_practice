from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(remain) means the min number of coins to change amount.
        memo = defaultdict(int)
        def dp(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in memo:
                return memo[remain]
            
            res = float('inf')
            for coin in coins:
                if remain-coin >= 0 and dp(remain-coin) != -1:
                    res = min(res, 1 + dp(remain - coin))
            memo[remain] = res if res != float('inf') else -1
            
            return memo[remain]
        
        return dp(amount)
