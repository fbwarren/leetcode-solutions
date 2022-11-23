def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    output = []
    queue = Deque([root])

    while queue:
        level = []
        length = len(queue)
        for _ in range(length):
            curr = queue.pop()
            level.append(curr.val)
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
        output.append(level)

    return output
