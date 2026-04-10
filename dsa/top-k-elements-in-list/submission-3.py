class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        buckets = [
            [] for i in range(len(nums) + 1)
        ]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in count.keys():
            buckets[count[num]].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
        