class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        A = defaultdict(list)
        for s in strs:
            sortedS=''.join(sorted(s))
            A[sortedS].append(s)
        return (list(A.values()))