# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        if root.left == None and root.right == None:
            return [root.val]
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            child_queue = deque()
            rightSide = -1
            while queue:
                curr = queue.popleft()
                if curr.left != None:
                    child_queue.append(curr.left)
                if curr.right != None:
                    child_queue.append(curr.right)
                rightSide = curr
            res.append(rightSide.val)
            queue = child_queue

        return res