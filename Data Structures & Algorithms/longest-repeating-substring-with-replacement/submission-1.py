class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={} # count of each character frequency

        l=0
        ans=0

        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1

            while (r-l+1)-max(count.values())>k: # window length-most frequent char
            # in order to be valid
            # you cannot have more replacements needed than k
                count[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
