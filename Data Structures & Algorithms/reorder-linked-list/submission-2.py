# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None # break the link between first and second half

        while curr: # reverse second half
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        
        left = head
        right = prev

        while left and right:
            dummy = left.next
            left.next = right

            left = dummy
            dummy = right.next

            right.next = left
            right = dummy