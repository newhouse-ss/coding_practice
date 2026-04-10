class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count + buckets
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums)+1)]

        for num, fre in count.items():
            buckets[fre].append(num)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res