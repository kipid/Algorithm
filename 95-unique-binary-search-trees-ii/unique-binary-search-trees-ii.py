# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
memo = {}
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        global memo
        def allPossibleBST(start,end):
            res = []
            if start > end:
                res.append(None)
                return res
            if (start,end) in memo:
                return memo[(start,end)]
            for i in range(start,end+1):
                leftSubTrees = allPossibleBST(start,i-1)
                rightSubTrees = allPossibleBST(i+1,end)

                for left in leftSubTrees:
                    for right in rightSubTrees:
                        node = TreeNode(i,left,right)
                        res.append(node)
            
            memo[(start,end)] = res
            return res
        return allPossibleBST(1,n)