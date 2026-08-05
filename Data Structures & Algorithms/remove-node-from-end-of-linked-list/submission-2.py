# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        
        find = count - n
        print(count, find)
        count = 0
        prev, curr = ListNode(next=head), head
        while curr:
            if count == find:
                if count == 0:
                    head = head.next
                prev.next = curr.next
                return head
            prev = prev.next
            curr = curr.next
            count += 1
