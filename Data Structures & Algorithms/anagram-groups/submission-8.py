from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I will maintain a hash table to solve this problem.
        # When meet a string s, apply ''.join(sorted(s)) on it,
        # if it's not in hash.keys(), create a key and append s
        # otherwise, append s into the existing hash[key].
        hash_table = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s)) # check on the unique key.
            hash_table[key].append(s)
        return list(hash_table.values())
