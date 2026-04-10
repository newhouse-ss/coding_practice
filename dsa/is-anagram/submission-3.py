class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # just use a dict to count? Another idea is substract char from another string.
        if len(s) != len(t):
            return False
        list_t = list(t)

        for char in s:
            if char in list_t:
                list_t.remove(char)
            else:
                return False
        
        return True