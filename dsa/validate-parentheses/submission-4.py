class Solution:
    def isValid(self, s: str) -> bool:
        """
        The main idea is: when we meet opening brackets, push in stack;
        when we meet closing brackets, check whether the stack top is the opening
        bracket match the closing bracket.
        """
        stack = []
        close_to_open = {'}':'{', ']':'[', ')':'('}

        for char in s:
            #closing bracket logic
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False