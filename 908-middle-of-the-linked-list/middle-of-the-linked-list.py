# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        r=head
        cnt=0
        while r:
            r=r.next
            cnt+=1
        cut=ceil(cnt//2)
        while cut>0:
            head=head.next
            cut-=1
        return head        