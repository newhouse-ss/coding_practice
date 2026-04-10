class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx = 0
        reslen = 0

        n = len(s)
        for i in range(n):

            # odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    reslen = r-l+1
                    residx = l
                
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    reslen = r-l+1
                    residx = l
                l -= 1
                r += 1
            
        return s[residx:residx+reslen]