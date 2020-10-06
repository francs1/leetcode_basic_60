class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        if root == None:
            return 0
        return self.pathSumWithRoot(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)

    def pathSumWithRoot(self,root,sum):
        if root == None:
            return 0
        ret = 0
        if root.val == sum:
            ret += 1
        ret += self.pathSumWithRoot(root.left,sum-root.val) + self.pathSumWithRoot(root.right,sum-root.val)
        return ret