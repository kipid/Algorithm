# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
memos = defaultdict(list)
def helper(left, right):    # construct trees using left->right numbers
    if left > right:
        return [None]
    if (left, right) in memos:
        return memos[(left, right)]
    for i in range(left, right+1):  # i can choose right, so the range is to right+1
        lefts = helper(left, i-1)
        rights = helper(i+1, right)
        for l in lefts:     # go through all the lefts and rights
            for r in rights:
                root = TreeNode(i, l, r)  # root created
                memos[(left, right)].append(root)
    return memos[(left, right)]    # just return the stored values
helper(1, 8)
class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        return helper(1, n)