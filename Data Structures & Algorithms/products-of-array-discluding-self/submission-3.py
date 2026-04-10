class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The main idea comes from: first calculate the product of all elements left of every i
        Then product the left product with the right product-->except product.
        """

        left, right = 1, 1
        res = [0]*len(nums)

        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        # all left product has been calculated, then iterate reversely to calculate right pro
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res