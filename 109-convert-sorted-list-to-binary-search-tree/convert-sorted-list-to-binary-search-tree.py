# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMid(head):
            prev, slow, fast = None, head, head
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            if prev:
                prev.next = None
            return slow

        if head == None:
            return None
        elif head.next == None:
            return TreeNode(head.val)
        
        mid = getMid(head)
        root = TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))
        return root