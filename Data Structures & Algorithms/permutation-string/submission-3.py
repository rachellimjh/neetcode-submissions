class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0]*26 # Index 0 is always "a" etc
        window = [0]*26

        for i in range(len(s1)):
            need[ord(s1[i])-ord('a')]+=1
            window[ord(s2[i])-ord('a')]+=1

        if need==window:
            return True
        
        for r in range(len(s1),len(s2)):
            window[ord(s2[r])-ord('a')]+=1
            window[ord(s2[r-len(s1)])-ord('a')]-=1 # s2[r-len(s1)] is char leaving window
            if need==window:
                return True
        return False