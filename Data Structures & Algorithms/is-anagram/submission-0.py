class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        length = len(s)
        for i in range(length):
            if s[i] in dict_s.keys():
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 0
            if t[i] in dict_t.keys():
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 0
        
        if dict_s.keys() != dict_t.keys():
            return False
        for key in dict_s.keys():
            if dict_s[key] != dict_t[key]:
                return False

        return True
            