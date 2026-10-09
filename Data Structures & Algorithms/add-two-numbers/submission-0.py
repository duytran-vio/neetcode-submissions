# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
        bor = 0
        while l1 or l2:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            sumDigit = val1 + val2 + bor
            bor = sumDigit // 10

            newNode = ListNode(sumDigit % 10)
            if tail is None:
                head = tail = newNode
            else:
                tail.next = newNode
                tail = newNode

            # move l1 and l2
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        if bor != 0:
            newNode = ListNode(bor)
            tail.next = newNode
        return head
            