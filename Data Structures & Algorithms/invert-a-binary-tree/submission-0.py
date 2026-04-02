# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swapBranch(self, root):
        if not root:
            return
        left = root.left
        right = root.right

        root.right = left
        root.left = right
        self.swapBranch(root.right)
        self.swapBranch(root.left)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swapBranch(root)
        return root

