class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next is None:
            return

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        second = prev
        first = head
        while second:
            nextFirst = first.next
            nextSecond = second.next
            second.next = nextFirst
            first.next = second
            second = nextSecond

            first = nextFirst