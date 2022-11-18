# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

**Main Idea**  
The largest diameter is always some path from a leaf node on the left to the root to a leaf node on the right.  
Use DFS to find the maximum depth of the left and right child, then sum them. Keep track of the maximum sum seen throughout DFS.

**Algorithm**  


```python
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
```

**Time complexity**  
$O(n)$ - we visit each node

**Space complexity**  
$O(1)$ - we only have our global variable
