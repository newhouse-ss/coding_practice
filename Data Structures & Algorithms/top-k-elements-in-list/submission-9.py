from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The idea comes from using a dict to record the frequence
        # of all unique numbers, then output the largest k of them.
        count = defaultdict(int)# initialized to 0
        for num in nums:
            count[num] += 1
        A = []
        for key, freq in count.items():
            A.append((freq, key))
        A.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(A[i][1]) # since k < distinct num of eles, and key is the value of eles, just return the k-most frequent.

        return res