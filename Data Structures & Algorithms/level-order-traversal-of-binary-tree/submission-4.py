# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = list()

        if not root:
            return level_order

        current_layer = [root]

        while True:
            move = False
            current_vals = []
            for node in current_layer:
                if node:
                    current_vals.append(node.val)
            level_order.append(current_vals)
            next_layer = []
            for node in current_layer:
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)

                    if node.left or node.right:
                        move = True

            if not move:
                break

            current_layer = next_layer


        return level_order