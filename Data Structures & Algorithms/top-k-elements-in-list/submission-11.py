from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # steps: find the freq of each key; put them into an array, sort by A[i][0], then iterate A for k times, keep output A[i][1]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        A = []
        for num, freq in count.items():
            A.append([freq, num])
        
        A.sort(reverse = True)
        res = []
        for i in range(k):
            res.append(A[i][1])
        
        return res