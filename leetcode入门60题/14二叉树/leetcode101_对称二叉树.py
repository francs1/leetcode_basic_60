class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root == None:
            return True
        return self.isSymmetric2(root.left,root.right)

    def isSymmetric2(self,left,right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetric2(left.left,right.right) and self.isSymmetric2(left.right,right.left)