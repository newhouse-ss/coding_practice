class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # It seems I can solve this problem in O(n^2), iterate the nums firstly, in each iteration, use two-pointers to explore the target.
        res = [] # used to record triples.
        nums.sort()

        n = len(nums)
        for i in range(n-2):
            target = -nums[i] # we need to sum this target in [nums[i+1]:]
            left, right = i+1, n-1
            while left < right:
                # strictly smaller since triples are unique
                if nums[left] + nums[right] == target:
                    choice = [nums[i], nums[left], nums[right]]
                    if choice not in res: #to make sure unique.
                        res.append(choice)
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1

        return res
