# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root,0)])
        res = defaultdict(int)
        while q:
            node, l = q.popleft()
            if node:
                res[l] = node.val
                q.append((node.left,l+1))
                q.append((node.right,l+1))

        return [res[l] for l in range(len(res))]