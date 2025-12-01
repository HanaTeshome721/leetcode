# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cnt=head
        while cnt:
            nxt=cnt.next
            cnt.next=prev
            prev=cnt
            cnt=nxt
        return prev    