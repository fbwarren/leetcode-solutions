def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1
