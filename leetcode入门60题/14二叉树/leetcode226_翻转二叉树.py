class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root