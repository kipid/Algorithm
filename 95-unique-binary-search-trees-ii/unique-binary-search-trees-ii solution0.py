from typing import Optional
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toList(self, preNodes):
        nextValues = []
        nextNodes = []
        for preNode in preNodes:
            if preNode.left:
                nextValues.append(preNode.left.val)
                nextNodes.append(preNode.left)
            if preNode.right:
                nextValues.append(preNode.right.val)
                nextNodes.append(preNode.right)
        if len(nextNodes) > 0:
            self.values.append(nextValues)
            self.nodes.append(nextNodes)
            self.toList(self.nodes[-1])

    def inorder(self, root, str_: str) -> str:
        if root:
            self.inorder(root.left, str_)
            self.str_ += str(root.val) + " "
            self.inorder(root.right, str_)
        return self.str_

    def __repr__(self):
        self.values = [[self.val]]
        self.nodes = [[self]]
        self.toList(self.nodes[-1])
        self.str_ = ""
        return f"{self.values}\ninorder: {self.inorder(self, '')}"
    # def __repr__(self):
    #     return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        @lru_cache
        def buildtree(left, right):
            if right < left:
                return [None]
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

sol = Solution()
lis = sol.generateTrees(8)
for li in lis:
    print(f"{li = }")
