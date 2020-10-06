class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        n = len(nums)
        if n == 0:#终止条件，返回空
            return None
        if n == 1:#终止条件，返回单节点
            return TreeNode(nums[0])
        mid = n // 2
        root = TreeNode(nums[mid])#将数组从中间一分为二
        root.left = self.sortedArrayToBST(nums[:mid])#左子树
        root.right = self.sortedArrayToBST(nums[mid+1:])#右子树
        return root#返回