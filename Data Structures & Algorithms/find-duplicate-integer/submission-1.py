class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyds algo:
        # 1. intersect fast and slow pointer, leave slow pointer there
        # 2. start another pointer from head, move until slow and head intersect
        # that would be the beginning of the cycle


        # each position is a pointer to another position's index

        slow,fast=0,0 # we know 0 is not part of the cycle

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]] # move fast twice
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow