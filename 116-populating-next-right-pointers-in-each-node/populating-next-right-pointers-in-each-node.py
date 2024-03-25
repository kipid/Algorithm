"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        curr = root
        while curr:
            prev, next = None, curr
            while next and next.left:
                next.left.next = next.right
                if prev:
                    prev.right.next = next.left
                prev, next = next, next.next
            curr = curr.left
        return root