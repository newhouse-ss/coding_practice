class Solution:
    def rob(self, nums: List[int]) -> int:
        # I think it's just a little different from I, the problem is how to choose the start?
        # key: just one of 0-th house and n-1-th house could be robbed.
        # just cut the length-n original array into 2 seperate: nums[:n-1]+nums[1:]
        # calculate maxi on them seperately, choose the max.
        n = len(nums)
        # pitfall: when n == 1, if we don't handle the edge case
        # nums1 and nums2 will be empty.
        if n == 1:
            return nums[0]
        
        nums1 = nums[:n-1]
        nums2 = nums[1:]
        memo1 = {}
        memo2 = {}
        
        def dp(i, numx, memox):
            if i == 0:
                return numx[0]
            if i == 1:
                return max(numx[1], numx[0])
            if i in memox:
                return memox[i]
            
            memox[i] = max(dp(i-1, numx, memox), dp(i-2, numx, memox) + numx[i])
            return memox[i]
        
        rob_0 = dp(len(nums1)-1, nums1, memo1)
        rob_last = dp(len(nums2)-1, nums2, memo2)

        return max(rob_0, rob_last)