class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count + minheap
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num, fre in count.items():
            heapq.heappush(heap, ([fre, num]))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])

        return res