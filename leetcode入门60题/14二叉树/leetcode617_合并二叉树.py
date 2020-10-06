class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if t1!=None or t2!=None:
            if t1==None:
                t1 = TreeNode(0)
            if t2==None:
                t2 = TreeNode(0)
            t = TreeNode(0)
            t.val = t1.val + t2.val
            t.left = self.mergeTrees(t1.left,t2.left)
            t.right = self.mergeTrees(t1.right,t2.right)
            return t

        return None