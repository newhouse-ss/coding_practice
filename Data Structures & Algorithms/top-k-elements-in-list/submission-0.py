class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            #check whether num is a key of count, if not, count[num] = 0
            count[num] = count.get(num, 0) + 1
        
        # hash table --> array to enable sort
        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()

        result = []

        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result