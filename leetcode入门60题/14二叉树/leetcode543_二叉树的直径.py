class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxnum = 0

    #隐含的前提，最大的距离应该是两个叶子节点的距离
    #本身这个函数是返回，当前节点到其所有叶子节点的最大深度
    def getLength(self,root):
        if root != None:
            #左子树的最大深度
            left = self.getLength(root.left)
            #右子树的最大深度
            right = self.getLength(root.right)
            #在返回之前，更新maxnum
            self.maxnum = max(self.maxnum,left+right)
            return 1 + max(left,right)
        return 0

    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        self.getLength(root)
        return self.maxnum