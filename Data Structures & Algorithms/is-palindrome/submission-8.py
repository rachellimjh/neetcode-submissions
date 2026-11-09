class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        while j>i:
            if not s[i].isalnum() or s[i]==" ":
                i+=1
                continue
            if not s[j].isalnum() or s[j]==" ":
                j-=1
                continue
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
                continue
            else:
                return False
        return True