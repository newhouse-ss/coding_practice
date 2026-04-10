class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The main idea comes from first transform the original input into lower alnum.
        # Then use a pair of pointers to iterate.
        cleaned = ''
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        n = len(cleaned)
        i, j = 0, n-1
        while i <= j:
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1
            else:
                break
        
        return True if i > j else False