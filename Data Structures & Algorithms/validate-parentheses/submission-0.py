class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s:
            # if c is a closing
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else: # if c is opening, just add to stack
                stack.append(c)
        
        # stack has to be empty
        return True if not stack else False
