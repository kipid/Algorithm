# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def buildtree(left, right):
            if right < left:
                return [None]
            if left == right:
                return [TreeNode(left)]
            trees = []
            for nd in range(left, right + 1):
                ltrees = buildtree(left, nd - 1)
                rtrees = buildtree(nd + 1, right)
                for ltree in ltrees:
                    for rtree in rtrees:
                        root = TreeNode(nd, ltree, rtree)
                        trees.append(root)
            return trees
        
        return buildtree(1, n)