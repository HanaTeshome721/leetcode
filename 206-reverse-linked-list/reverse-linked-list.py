# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # prev,cur=None,head
        # while cur:
        #    nxt=cur.next
        #    cur.next=prev
        #    prev=cur
        #    cur=nxt
        # return prev  


        if not head:
            return None
        newhead=head
        if head.next:
              newhead=self.reverseList(head.next)
              head.next.next=head
              head.next=None
        return newhead          