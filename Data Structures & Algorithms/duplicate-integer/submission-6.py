class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # since we just need to keep track of existence
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

