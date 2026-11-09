class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana = defaultdict(list)
        # {"a","c","e": ["ace", "cae"]}
        
        for word in strs:
            chars = tuple(sorted(word))
            ana[chars].append(word)
        
        return list(ana.values())