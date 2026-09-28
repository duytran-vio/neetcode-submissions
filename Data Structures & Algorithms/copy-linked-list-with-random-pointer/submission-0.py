"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.H = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.H:
            return self.H[head]

        node = Node(head.val)
        self.H[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.H.get(head.random)
        return node


