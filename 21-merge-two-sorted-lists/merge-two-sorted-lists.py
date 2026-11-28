# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        new=dummy
        l1=list1
        l2=list2
        while l1 and l2:
            if l1.val<l2.val:
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new=new.next    
        if l2:
            new.next=l2
        if l1:
            new.next=l1   
        return dummy.next               
