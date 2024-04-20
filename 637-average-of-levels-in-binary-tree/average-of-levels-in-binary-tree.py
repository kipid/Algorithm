# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        nodes = [[root]]

        def addLevel(preNodes: List[TreeNode]) -> List[TreeNode]:
            res = []
            for preNode in preNodes:
                if preNode.left:
                    res.append(preNode.left)
                if preNode.right:
                    res.append(preNode.right)
            return res
        
        while (curNodes := addLevel(nodes[-1])):
            nodes.append(curNodes)
        
        res = []        
        for curNodes in nodes:
            sum = 0
            for curNode in curNodes:
                sum += curNode.val
            res.append(sum / len(curNodes))
        
        return res