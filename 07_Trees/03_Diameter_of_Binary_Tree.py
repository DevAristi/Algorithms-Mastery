class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.res = 0

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res