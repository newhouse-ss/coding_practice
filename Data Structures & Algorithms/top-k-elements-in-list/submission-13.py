from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to solve this, firstly I need to know the frequencies.
        # So I use a hash table to count this, then include the
        # freq and number in a nested array, sort by freq
        # return the top-k.
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