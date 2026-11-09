class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
       
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
       
        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        # Sliding window
        for i in range(len(s2) - len(s1)):
            if matches == 26: return True
            
            # r is the character entering, l is the character leaving
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')

            # 1. Update Right (Adding a character)
            s2Count[r] += 1
            if s2Count[r] == s1Count[r]: matches += 1
            elif s2Count[r] == s1Count[r] + 1: matches -= 1

            # 2. Update Left (Removing a character)
            s2Count[l] -= 1
            if s2Count[l] == s1Count[l]: matches += 1
            elif s2Count[l] == s1Count[l] - 1: matches -= 1

        return matches == 26