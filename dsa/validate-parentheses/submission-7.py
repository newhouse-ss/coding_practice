class Solution:
    def isValid(self, s: str) -> bool:
        """
        main idea: every time meet a opening bracket, push in stack; enerytime meet
        a closing brackets, check whether the element at the top of stack match.
        """
        close_to_open = {'}':'{', ']':'[', ')':'('}
        stack = []

        for par in s:
            if par in close_to_open:
                if stack and stack[-1] == close_to_open[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
            
        return True if not stack else False