class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add ( if open<n
        # only add ) if closed<open
        # well-formed iff open==closed==n

        res=[]
        stack=[] # what we are currently building

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res