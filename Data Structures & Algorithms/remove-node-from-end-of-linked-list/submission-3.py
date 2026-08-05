# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left, right = dummy, head

        c = 0
        while c < n:
            right = right.next
            c += 1
        
        while right:
            right = right.next
            left = left.next
        
        if left == dummy:
            head = head.next
            return head
        left.next = left.next.next
        return head
