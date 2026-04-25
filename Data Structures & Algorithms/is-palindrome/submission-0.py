class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cheating solution
        # by using inbuilt functions 
        # uses extra space to reverse the string too
        newStr=""

        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        
        return newStr == newStr[::-1] # reverse the string