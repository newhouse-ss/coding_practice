class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i in range(len(nums)):
            component = target-nums[i]
            if component in hashtable:
                return [hashtable[component], i]
            
            hashtable[nums[i]] = i