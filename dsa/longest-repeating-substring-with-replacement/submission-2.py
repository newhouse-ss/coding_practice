from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        fre = defaultdict(int)
        res = 0

        for r in range(n):
            fre[s[r]] += 1
            most_fre = max(fre.values())
            while (r - l + 1) - most_fre > k:
                fre[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res