class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The idea comes from left-product and right-product,
        # If I keep producting num onto 1 while iterating nums, I can make sure output[i] is the product of all element on left of nums[i]
        n = len(nums)
        output = [0]*n

        left_pro = 1 # product of all nums before nums[i]
        for i in range(n):
            output[i] = left_pro
            left_pro *= nums[i] #build loop invariant for nums[i+1]

        right_pro = 1 # product of all nums after nums[i]
        for i in range(n-1, -1, -1):
            output[i] *= right_pro
            right_pro *= nums[i]
        
        return output