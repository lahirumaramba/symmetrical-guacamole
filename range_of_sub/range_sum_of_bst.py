# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        """def dfs(node):
            if node is None:
                return

            if node.val >= L and node.val <= R:
                self.ans += node.val

            if node.val < R:
                dfs(node.right)

            if node.val > L:
                dfs(node.left)

        self.ans = 0
        dfs(root)
        return self.ans"""

        nodes = [root]
        total = 0

        while nodes:
            node = nodes.pop(-1)
            if node.val >= L and node.val <= R:
                total += node.val

            if node.left and node.val > L:
                nodes.append(node.left)

            if node.right and node.val < R:
                nodes.append(node.right)

        return total
