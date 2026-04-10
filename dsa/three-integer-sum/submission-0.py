class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        brute force: iterate all possible triples, since there's no
        repetitive in the result, first make a set
        """
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        
        return [list(i) for i in res]