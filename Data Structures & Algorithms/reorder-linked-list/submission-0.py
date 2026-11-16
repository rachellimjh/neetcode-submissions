# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split list into 2 halfs at the middle
        # reverse second half 

        # finding the middle of the list
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse second
        second=slow.next
        slow.next=None # cut list into 2
        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt

        # merge 2 halfs
        first,second=head,prev

        while first and second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2


