class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # It fits all features to apply DP
        # dp-function: dp(i) means the len of longest consecutive sequence end with i-th num.
        # Some how like LIS, because the result DO NOT NEED TO BE CONTINUOUS. this pattern means I need to explore all dp(j) where j < i to result dp(i).
        # recurrence: dp(i) = max(1, dp(j)+1 for j in range(i) if nums[i] == nums[j] + 1)
        # base case: i == 1, return 1
        
        #pitfall:  The elements do not have to be conasecutive in the original array.
        #This means we can form the initial input in any order.(set+sort)
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) == 1:
            return 1
            
        memo = {}
        self.res = 0

        def dp(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]
            
            res = 1 # res = 1 is important, if no i, j pair fits the relationship bellow, res is the edge case.
            for j in range(i):
                if nums[i] == nums[j] + 1:
                    res = max(res, dp(j) + 1) # if nums[i] is larger than nums[j] by exactly 1, we can expand the length of LCS.
                    
            memo[i] = res
            self.res = max(self.res, memo[i])
            return memo[i]
        
        n = len(nums)
        for i in range(n):
            dp(i) # pitfall: I need to explore all cases.
        
        return self.res
        # return dp(n-1) #pitfall: the LCS maybe not end with nums[n-1]