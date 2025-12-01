# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ls=ListNode()
        gt=ListNode()
        l=ls
        g=gt
        while head:
            if head.val<x:
                ls.next=head
                ls=ls.next
            else:
                gt.next=head
                gt=gt.next
            head=head.next  
        gt.next=None
        ls.next=g.next
        return l.next
