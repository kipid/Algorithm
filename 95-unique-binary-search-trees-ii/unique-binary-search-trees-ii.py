# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
dp = defaultdict(list)
def helper(left, right):    # construct trees using left->right numbers
    if left > right:
        return [None]
    if (left, right) in dp:
        return dp[(left, right)]
    for i in range(left, right+1):  # i can choose right, so the range is to right+1
        lefts = helper(left, i-1)
        rights = helper(i+1, right)
        for l in lefts:     # go through all the lefts and rights
            for r in rights:
                root = TreeNode(i)  # root created
                root.left = l
                root.right = r
                dp[(left, right)].append(root)
    return dp[(left, right)]    # just return the stored values
helper(1, 8)
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # using explicit memoization (not using lru_cache), just recursion. we can split into left trees and right trees.
        # we pick a node, the numbers on the left will make left trees, the numbers on the
        # right will make right trees.
        # we use memoization to store the intermediate results
        return dp[(1, n)]