# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,next=head)
        prev=dummy
        cnt=head
        while cnt:
            # nxt=cnt.next
            if cnt.val==val:
                prev.next=cnt.next
            else:
                prev=cnt
            cnt=cnt.next
        return dummy.next            