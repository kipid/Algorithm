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
            fast = head
            slow = head
            prev = None
            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            if prev:
                prev.next = None
            return slow

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        mid = getMid(head)
        root = TreeNode(mid.val)

        leftTree = self.sortedListToBST(head)
        rightTree = self.sortedListToBST(mid.next)
        root.left = leftTree
        root.right = rightTree
        return root