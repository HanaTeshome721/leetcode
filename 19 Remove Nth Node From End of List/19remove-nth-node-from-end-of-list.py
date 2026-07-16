# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=head
        dummy=ListNode(next=head)
        c=0
        while cnt:
            c+=1
            cnt=cnt.next
        r=c-n
        l=dummy
        # cnt=head
        for i in range(r):
            l=l.next
            # cnt=cnt.next
        l.next=l.next.next
        return  dummy.next   

        # dummy=ListNode(next=head)
        # r=head
        # l=dummy
        # while n:
        #     r=r.next
        #     n-=1
        # while r:
        #     r=r.next
        #     l=l.next
        # l.next=l.next.next

        # return dummy.next       