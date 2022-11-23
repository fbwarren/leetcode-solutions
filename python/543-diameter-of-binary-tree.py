def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        self.output = max(self.output, left + right)

        return max(left, right) + 1

    self.output = 0
    dfs(root)

    return self.output
