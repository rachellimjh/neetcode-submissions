class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        curr=[]
        # probably need to store the mapping first?
        digitToChar= {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i):
            if i==len(digits):
                res.append("".join(curr[:]))
                return
            for char in digitToChar[digits[i]]:
                curr.append(char)
                dfs(i+1)
                curr.pop()
        if digits:
            dfs(0)

        return res
