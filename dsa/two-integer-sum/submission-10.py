class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        res = []
        for i, num in enumerate(nums):
            res.append([num, i])
        res.sort()

        while left < right:
            if target == res[left][0] + res[right][0]:
                return [min(res[left][1], res[right][1]), max(res[left][1], res[right][1])]
            elif target < res[left][0] + res[right][0]:
                right -= 1
            else:
                left += 1