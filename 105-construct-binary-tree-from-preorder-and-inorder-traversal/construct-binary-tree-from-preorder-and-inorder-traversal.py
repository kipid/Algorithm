# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = { v:i for i,v in enumerate(inorder) } # v -> inorder index

        curr_node_preorder_index = 0

        def buildTree(left, right):
            if left > right:
                return None
            
            nonlocal curr_node_preorder_index
            curr_node_value = preorder[curr_node_preorder_index]
            curr_node_inorder_index = inorder_map[curr_node_value]

            curr_node = TreeNode(curr_node_value)
            curr_node_preorder_index += 1

            curr_node.left = buildTree(left, curr_node_inorder_index-1)
            curr_node.right = buildTree(curr_node_inorder_index+1, right)
            return curr_node

        return buildTree(0, len(inorder)-1)