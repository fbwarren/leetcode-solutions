def isBalanced(root: Optional[TreeNode]) -> bool:
    self.output = True

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) > 1:
            self.output = False
        return max(left, right) + 1

    dfs(root)
    return self.output
