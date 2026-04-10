class Solution:
    def isValid(self, s: str) -> bool:
        # The idea comes from using a stack to track the left
        # parentheses, everytime meet a right parentheses, pop
        # from stack and check whether it's a pair with right.
        stack = []
        rules = {
            "(" : ")", 
            "{" : "}", 
            "[" : "]"
        }
        if s[0] in rules.values():
            return False

        for char in s:
            if char in rules:
                stack.append(char)
                continue
            if char in rules.values():
                if not stack:
                    return False #pitfall
                left = stack.pop()
                if rules[left] != char:
                    return False

        return True if not stack else False # Pitfall: if all parentheses are match, empty stack.