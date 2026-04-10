class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp-function: dp(i) means the max amount of money I can rob up to and including i-th house.
        # recurrence: dp(i) = max(dp(i-1), dp(i-2) + nums[i])
        # base case: if i == 0: return nums[0]; if i == 1: return max(nums[0], nums[1])
        memo = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        
        n = len(nums)
        return dp(n-1)