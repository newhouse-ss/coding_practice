from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The main idea comes from: When we meet a string, use a 
        hash table to record the frequency of each character.
        Then regard this hash table as the key of the result, 
        strings have the same frequency will be added into the 
        list after the hash table key.
        """
        # if no such key in list, initialize with this key and
        # a list as value
        res = defaultdict(list)
        for string in strs:
            count = [0]*26
            for s in string:
                count[ord(s) - ord('a')] += 1
            res[tuple(count)].append(string)
        
        return list(res.values())