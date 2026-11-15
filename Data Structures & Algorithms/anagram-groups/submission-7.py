class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list) # (a,c,t): ["act", "cat"]

        for word in strs:
            chars=sorted(list(word))
            chars=tuple(chars)
            
            ana[chars].append(word)

        return list(ana.values())