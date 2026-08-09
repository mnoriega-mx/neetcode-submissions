# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        
        # move pointers
        l, r = head, prev
        while l and r:
            left_next = l.next
            l.next = r

            right_next = r.next
            r.next = left_next

            l = left_next
            r = right_next