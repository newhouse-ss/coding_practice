class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash table to count the frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # maintain a min_heap
        heap = []

        for key in count.keys():
            heapq.heappush(heap, (count[key], key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        # k-most frequent nums are stored in heap
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result