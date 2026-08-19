# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, curr = None, head

            while curr and k > 0:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                k -= 1
            
            return prev


        root = ListNode()
        prevGroup = root
        curr = tail = head

        while curr:
            tail = curr

            idx = 0
            while curr and idx < k:
                curr = curr.next
                idx += 1

            tmp = tail
            if idx == k:
                prevGroup.next = reverse(tail, k)
            else:
                prevGroup.next = tail
            
            prevGroup = tmp
        
        return root.next