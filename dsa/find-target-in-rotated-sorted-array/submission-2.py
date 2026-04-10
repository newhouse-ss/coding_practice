class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # 左半段有序
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # target 在左半段
                else:
                    l = m + 1  # target 在右半段
            # 右半段有序
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1  # target 在右半段
                else:
                    r = m - 1  # target 在左半段
        
        return -1