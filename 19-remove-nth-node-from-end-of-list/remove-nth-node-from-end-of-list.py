# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cnt=1
        crn=head
        while crn.next:
            cnt+=1
            crn=crn.next
        rn=cnt-n
        if rn==0:
            return head.next
        cnt=head
        i=0
        while cnt and i<rn-1 :
            cnt=cnt.next
            i+=1
        if not cnt or not cnt.next:
            return head
        cnt.next=cnt.next.next  

        return head  
         