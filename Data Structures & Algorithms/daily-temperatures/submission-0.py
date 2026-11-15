class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # indices of days still waiting for a warmer day
        # pair : [temp, index]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp,stackindex=stack.pop()
                res[stackindex]=i-stackindex
            stack.append([t,i])
    
        return res