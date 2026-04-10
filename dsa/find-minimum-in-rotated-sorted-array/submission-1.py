class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial: return min(nums)
        # return min(nums), this is boring, try to apply binary search.
        # To apply binary search, the prerequisite is: The array should be sorted. But if the array is sorted why we need binary search??? (nums[0] is min), so we need to use binary search find the cut-point.
        n = len(nums)
        left, right = 0, n-1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right)//2
            res = min(res, nums[mid])
            # notice now, nums[left]>nums[right]
            if nums[left] <= nums[mid]:
                # left part is sorted, what we find is the non-sorted part, go right
                left = mid + 1
            else:
                #nums[left] > nums[mid], left part is not sorted, go left.
                right = mid-1
        return res