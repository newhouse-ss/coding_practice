from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = [] # to store tuples: (ordered_str, str)
        for string in strs:
            ordered = sorted(string)
            ordered_str = ''.join(ordered)
            A.append((string, ordered_str))
        
        res = defaultdict(list)
        for string, ordered_str in A:
            res[ordered_str].append(string)
        
        return list(res.values())
