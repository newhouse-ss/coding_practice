class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The main idea comes from: set + mannually consecutive + live updating
        """
        set_nums = set(nums)
        maxi = 0
        for num in set_nums:
            cnt = 1
            consec = num + 1
            while consec in set_nums:
                cnt += 1
                consec += 1
            if cnt > maxi:
                maxi = cnt
        
        return maxi