class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        heterogeneous = set(nums)
        if len(heterogeneous)<len(nums):
            return True
        
        return False