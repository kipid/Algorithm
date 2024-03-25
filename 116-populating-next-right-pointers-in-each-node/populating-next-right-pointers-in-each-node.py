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

        rowNodes = [[root]]

        def nextLevel(preNodes: List[TreeNode]) -> bool:
            nextNodes = []
            for preNode in preNodes:
                if preNode.left:
                    nextNodes.append(preNode.left)
                if preNode.right:
                    nextNodes.append(preNode.right)
            if len(nextNodes) > 0:
                rowNodes.append(nextNodes)
                return True
            else:
                return False
        
        while nextLevel(rowNodes[-1]):
            pass
        for rowNode in rowNodes:
            for i in range(len(rowNode)-1):
                rowNode[i].next = rowNode[i+1]
        return root