# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val  # Initialize a list to store the result

        def DFS(root):
            if root == None:
                return 0  # Base case: return 0 if the node is None

            # Recursive calculation for left and right subtrees
            # Ensure that negative values are not considered (max(0, ...))
            lmax = max(0, DFS(root.left))
            rmax = max(0, DFS(root.right))

            nonlocal ans
            # Update the overall maximum path sum
            ans = max(ans , root.val + lmax + rmax)

            # Return the maximum path sum that starts from the current node
            return root.val + max(lmax , rmax)

        # Call the DFS function on the root node
        DFS(root) 

        # Return the final maximum path sum
        return ans