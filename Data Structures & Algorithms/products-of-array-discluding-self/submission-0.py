class Solution:
    def except_product(self, arr, i):
        """
        Except i-th element from arr, then calculate product
        """
        temp = arr[:i] + arr[i+1:]

        prod = 1
        for num in temp:
            prod *= num

        return prod

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(self.except_product(nums, i))
        
        return res