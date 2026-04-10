from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        # No substring like: '30'.
        # DP: 1. num of ways; 2. The current decode choice affect the future choices.
        # dp-function: dp(i) means the num of ways to decode the
        # substring up to and including the i-th char.
        # recurrence: 1. choices: '0' or '1~9', if the current digit in range(1, 9), it
        # could be decoded directly, or it can be regard as a part of the former digit.
        # 2. transitions: dp(i) = dp(i-1) + dp(i-2); if s[i] == '0', it can not be decoded
        # independently, has to be a part of former digit.
        # base case: i == 0, s[i] != 0, 1; i==0, s[i] == 0, 0; i < 0, 0.
        memo = defaultdict(int)
        def dp(i):
            if i == 0:
                return 1 if s[i] != '0' else 0
            if i < 0:
                return 1 #pitfall
            if i in memo:
                return memo[i]
            # decode independently
            if s[i] != '0':
                memo[i] += dp(i-1)
            # decode as a part of the former
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                memo[i] += dp(i-2)
            return memo[i]
        
        n = len(s)
        return dp(n-1)