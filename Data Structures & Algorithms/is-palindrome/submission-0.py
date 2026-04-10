from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        First clean the string, then use deque to check whether parlidrome.
        """
        cleaned = deque()
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        
        while cleaned:
            # odd
            if len(cleaned) == 1:
                return True
            left = cleaned.popleft()
            right = cleaned.pop()
            if left != right:
                return False
        # even
        return not cleaned