class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if not (s[l].isalnum() and s[l]!=' '):
                l+=1
                continue
            if not (s[r].isalnum() and s[r]!=' '):
                r-=1
                continue
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
                continue
            else:
                return False
        return True
