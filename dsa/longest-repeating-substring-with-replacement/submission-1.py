
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The idea comes from maintaining the frequence of the most frequent character within the window, if length-frequence > k, increase the left boundry.
        # so use a hash table to track the frequence. The is a classic pattern for 不定长滑动窗口，右侧用for循环持续增长即可，
        n = len(s)
        fre = defaultdict(int)
        res = 0
        l = 0

        for r in range(n):
            fre[s[r]] += 1
            most_fre = max(fre.values())
            while r - l + 1 - most_fre > k: # not sufficient to flip all, decrease window size.
                fre[s[l]] -= 1
                l += 1
                most_fre = max(fre.values())
            res = max(res, r - l + 1)
        
        return res