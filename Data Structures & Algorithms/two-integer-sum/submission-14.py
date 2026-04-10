class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The brute force time complexity is O(n^2)
        # If we can sort the nums before exploration, O(nlgn)
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort() #sorted by number

        i, j = 0, len(A)-1
        while i<j:
            if A[i][0] + A[j][0] == target:
                res = [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
                return res
            if A[i][0] + A[j][0] > target:
                j -= 1
            if A[i][0] + A[j][0] <  target:
                i += 1