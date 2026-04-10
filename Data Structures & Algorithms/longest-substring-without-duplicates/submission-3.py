from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        n = len(s)
        # use a dict to record the indices of the unique char.
        unique = defaultdict(int)

        for r in range(n):
            if s[r] not in unique:
                unique[s[r]] = r # this is the first time meet  s[r], record its position
            
            else:
                l = max(l, unique[s[r]] + 1) # recoding the previous index of s[r], move l to unique[s[r]] + 1
                unique[s[r]] = r
            
            res = max(res, r - l + 1)
        
        return res