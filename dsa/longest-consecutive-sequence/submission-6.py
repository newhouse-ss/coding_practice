class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Though it's OK to simulate LIS and use DP to solve this question, but since there's a constriction on consecutive
        # The optimal solution is hashset. The idea comes from: If nums[i]-1 not in set, nums[i] must be the beginning of a consecutive sequence.
        nums = set(nums)
        if not nums:
            return 0
            
        res = 1
        for num in nums:
            if num-1 not in nums:
                curr_head = num
                curr_len = 1

                while curr_head + 1 in nums:
                    curr_len += 1
                    curr_head += 1
                
                res = max(res, curr_len)

        return res