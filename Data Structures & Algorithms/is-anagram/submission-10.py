from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for char in s:
            count_s[char] += 1 
        for char in t:
            count_t[char] += 1
            
        if count_s.keys() != count_t.keys():
            return False
        for key in count_s:
            if count_s[key] != count_t[key]:
                return False
        
        return True