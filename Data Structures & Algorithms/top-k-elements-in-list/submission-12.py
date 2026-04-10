from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k =  Counter(nums).most_common(k)
        res = []
        for i in range(k):
            res.append(top_k[i][0])
        
        return res