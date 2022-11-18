# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

**Main Idea**  
This is essentially bfs with extra steps.

**Algorithm**  
Use a `Deque()` (queue) to perform bfs.  
Since you want to create a list of lists, where each list contains the values for a specific level, you can't just go through bfs as normal.  
Every time we start to process a level, we first check the length of the queue since it only contains all of the nodes for the current level. Then, we process only that many nodes and add them to `level` while still adding their children to the queue.  


```python
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
```

**Time complexity**  
$O(n)$ since we visit every node once

**Space complexity**  
$O(n)$ since `level` and `queue` depend on the number of nodes  
(the number of leaves in a full binary tree is $\frac{n+1}{2}$)
