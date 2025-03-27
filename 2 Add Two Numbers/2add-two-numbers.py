# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify result list handling
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 or 0 if None
            val2 = l2.val if l2 else 0  # Get value from l2 or 0 if None
            total = val1 + val2 + carry
            
            carry, digit = divmod(total, 10)  # Compute carry and digit
            current.next = ListNode(digit)  # Append new node to result
            current = current.next  # Move to next node

            # Move to next nodes in input lists if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return head of result list