# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m, ptr = 0, head
        while ptr:
            m += 1
            ptr = ptr.next
        
        ptr, index, prev = head, 0, None
        while index < m - n:
            index += 1
            prev = ptr
            ptr = ptr.next

        if ptr == head:
            return head.next
        prev.next = ptr.next
        return head
        