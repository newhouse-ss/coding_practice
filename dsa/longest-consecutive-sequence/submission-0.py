class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        temp = set(nums)

        for num in nums:
            streaker, cur = 0, num
            while cur in temp:
                streaker += 1
                cur += 1
            res = max(res, streaker)

        return res