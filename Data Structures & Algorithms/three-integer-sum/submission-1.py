class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        two pointers
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum_3 = a + nums[left] + nums[right]
                if sum_3 > 0:
                    right -= 1
                elif sum_3 < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
