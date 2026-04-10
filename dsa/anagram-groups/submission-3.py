class Solution:
    def is_Anagrams(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        return sorted(str1) == sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while strs:
            temp = []
            temp.append(strs[0])
            
            for i in range(1,len(strs)):
                if self.is_Anagrams(strs[0], strs[i]):
                    temp.append(strs[i])
            
            res.append(temp)
            for _ in temp:
                strs.remove(_)

        return res