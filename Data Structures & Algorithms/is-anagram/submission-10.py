class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashT = [0]*26 
        hashS = [0]*26

        for c in s:
            i=ord(c)-ord('a')
            hashS[i]+=1
        for d in t:
            i=ord(d)-ord('a')
            hashT[i]+=1

        if hashT==hashS:
            return True
        return False