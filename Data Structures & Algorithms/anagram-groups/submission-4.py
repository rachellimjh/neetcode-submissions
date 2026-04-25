class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        # key: characters 
        # value: string

        res = defaultdict(list)
        for s in strs:
            char=[0]*26
            for c in s:
                char[ord(c)-ord('a')]+=1
            res[tuple(char)].append(s) # must append if not will overwrite
        return list(res.values())
        
