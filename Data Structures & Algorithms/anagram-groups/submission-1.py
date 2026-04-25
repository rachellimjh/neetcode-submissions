class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        A = defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            A[tuple(count)].append(s)

        return list(A.values())