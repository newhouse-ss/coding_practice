class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min is on the cut-point.
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                # the cut-point in right half
                left = mid + 1
            else:
                right = mid

        return nums[left]