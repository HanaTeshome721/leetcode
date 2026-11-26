# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy=ListNode()
        if not head:
            return None
        dummy.next=head
        current=head
        prev=dummy
        while current:            
            nxt=current.next
            if current.val==val:
                prev.next=nxt
            else:
                prev=current
            current=current.next         
        return dummy.next         