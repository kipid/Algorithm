from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def iterativeInorder(root):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val, end=" ")
            root = root.right

def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def iterativePreorder(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        print(root.val, end=" ")
        # right child is pushed first so that left is processed first
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

def iterativePostorder(root):
    stack = []
    lastNodeVisited = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            peekNode = stack[-1]
            # if right child exists and traversing root from left child, then move right
            if peekNode.right and lastNodeVisited != peekNode.right:
                root = peekNode.right
            else:
                print(peekNode.val, end=" ")
                lastNodeVisited = stack.pop()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

inorder_traversal(root) # 2 3 4 5 8
print()
iterativeInorder(root) # 2 3 4 5 8
print()

preorder_traversal(root) # 5 3 2 4 8
print()
iterativePreorder(root) # 5 3 2 4 8
print()

postorder_traversal(root) # 2 4 3 8 5
print()
iterativePostorder(root) # 2 4 3 8 5
print()