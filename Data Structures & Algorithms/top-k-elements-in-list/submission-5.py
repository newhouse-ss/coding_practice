class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count + sort
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = []
        for num, fre in count.items():
            arr.append([fre, num])
        
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])

        return res