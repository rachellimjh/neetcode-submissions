class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack=[] # stack

        for ch in s:
            if ch in pairs: # closing bracket (check for key)
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        if stack:
            return False

        return True
        
