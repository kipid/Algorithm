# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        nodesRes = [[root]]
        def addLevel(levelRoots: List[TreeNode]) -> Optional[List[TreeNode]]:
            nodeValues = []
            nodes = []
            for levelRoot in levelRoots:
                if levelRoot.left:
                    nodes.append(levelRoot.left)
                    nodeValues.append(levelRoot.left.val)
                if levelRoot.right:
                    nodes.append(levelRoot.right)
                    nodeValues.append(levelRoot.right.val)
            if len(nodeValues) > 0:
                res.append(nodeValues)
                nodesRes.append(nodes)
                return True
            return False
        while addLevel(nodesRes[-1]):
            pass
        return res