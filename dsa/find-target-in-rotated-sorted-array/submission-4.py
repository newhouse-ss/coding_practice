class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The key idea is just one thing, don't see the bullshit answer.
        # Just simply apply binarysearch, the idea is: in the left part of mid or right part of mid, one of them is sorted.
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[left]:
                #左边一定有序
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #右边一定有序
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1