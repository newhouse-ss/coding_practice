class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        nums_set = set(nums)
        len_set = len(nums_set)

        if len_list > len_set:
            return True

        return False