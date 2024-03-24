# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        # Create a hashmap to store the indices of elements in the inorder list
        inorder_map = {val: index for index, val in enumerate(inorder)}

        # Define a recursive function to build the binary tree
        def build(pre_start, pre_end, in_start, in_end):
            # Base case: If the start index in the preorder list is greater than the end index,
            # it indicates that the current subtree is null, so return None
            if pre_start > pre_end:
                return None

            # Extract the value of the root node from the preorder list using the start index
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find the index of the root node's value in the inorder list using the hashmap
            in_index = inorder_map[root_val]

            # Determine the size of the left subtree
            left_size = in_index - in_start

            # Recursively build the left subtree
            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_index - 1)

            # Recursively build the right subtree
            root.right = build(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

            return root

        # Call the build function with initial parameters corresponding to the entire preorder and inorder lists
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)