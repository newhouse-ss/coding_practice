class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP: 1. largest; 2. Whether include the current ele in
        # arr or not affect the future selection.
        # dp-function: dp(i) means the largest or smallest product of the subarray upto and including i-th num.
        # recurrence: 1. choices: if current is +, product the maxi, if current is -, product the mini.
        # 2. transition: if nums[i] > 0: maxi = nums[i]*dp(i-1)[0], mini = , if nums[i]<0: maxi = 
        # base case: if i == 0: return nums[0] if nums[0]>0 else 0.
        memo = {}
        self.res = float('-inf')
        def dp(i): # the return value is a tuple.
            if i == 0:
                self.res = max(self.res, nums[i])
                return nums[i], nums[i]
            if i in memo:
                return memo[i]
            
            maxi, mini = dp(i-1)[0], dp(i-1)[1]
            curr_max = max(nums[i], nums[i]*maxi, nums[i]*mini)
            curr_min = min(nums[i], nums[i]*maxi, nums[i]*mini)
            memo[i] = (curr_max, curr_min)

            self.res = max(self.res, curr_max)
    
            return curr_max, curr_min
        
        n = len(nums)
        dp(n-1)
        return self.res