# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = { val:i for i, val in enumerate(inorder)}

        def build(post_end: int, in_start: int, in_end: int) -> (TreeNode | None, int):
            if in_start >= in_end:
                return None, post_end
            
            root_val = postorder[post_end]
            root_index = inorder_index[root_val]
            
            r_tree, post_start = build(post_end - 1, root_index + 1, in_end)
            l_tree, post_start = build(post_start, in_start, root_index)
            
            return TreeNode(root_val, l_tree, r_tree), post_start
        
        return build(len(postorder) - 1, 0, len(inorder))[0]