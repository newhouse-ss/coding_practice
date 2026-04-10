class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 二分查找是更快速的方法，但是不能用的原因是现在并非有序
        # 所以先排序；但是题目要求返回下标，暴力排序的话会丢失信息
        # 所以先使用嵌套数组记录所有元素和下表，然后对元素值排序
        # 二分查找
        A = []
        for idx, num in enumerate(nums):
            A.append([num, idx])
        A.sort()

        n = len(A)
        l, r = 0, n-1
        while l <= r:
            if A[l][0] + A[r][0] > target:
                r -= 1
            elif A[l][0] + A[r][0] < target:
                l += 1
            else:
                return sorted([A[l][1], A[r][1]])
        
        return False