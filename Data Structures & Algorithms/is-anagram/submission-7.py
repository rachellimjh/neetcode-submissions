class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashT = [0]*26
        hashS = [0]*26

        for c in s:
            hashS[ord(c)-ord('a')]+=1
        for c in t:
            hashT[ord(c)-ord('a')]+=1
        
        if hashT==hashS:
            return True
        return False