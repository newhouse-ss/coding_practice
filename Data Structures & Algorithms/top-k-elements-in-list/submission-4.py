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
        pointer = len(arr) - 1
        while len(res) < k:
            if pointer < 0:
                return res
            res.append(arr[pointer][1])
            pointer -= 1

        return res