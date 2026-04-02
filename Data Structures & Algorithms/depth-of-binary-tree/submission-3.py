# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.maxDepth(root.left, depth + 1)
        if root.right:
            right_depth = self.maxDepth(root.right, depth + 1)
        return max(1 + self.maxDepth(root.left, 0), 1 + self.maxDepth(root.right, 0))