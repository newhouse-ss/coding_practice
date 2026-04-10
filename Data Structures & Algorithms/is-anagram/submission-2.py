class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        The main idea comes from: 
        """
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)