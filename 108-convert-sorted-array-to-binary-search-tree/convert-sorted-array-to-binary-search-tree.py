# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            # if left == right:
            #     return TreeNode(nums[left])
            # elif left+1 == right:
            #     return TreeNode(nums[right], TreeNode(nums[left]))
            mid = (left + right) // 2
            root = TreeNode(nums[mid], helper(left, mid-1), helper(mid+1, right))
            return root
        
        return helper(0, len(nums)-1)