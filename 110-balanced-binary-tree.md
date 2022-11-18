# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

**Main Idea**  
DFS and have a global variable that changes false if an unbalanced tree is found.

**Algorithm**  
Pretty much just use DFS to find the height of the left and right subtrees. If their height is different by greater than one, set your global variable to false. Either way, return the height plus one so that the parent can compare its childrens heights.

```python
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
```

**Time complexity**  
$O(n)$ - we process every node.

**Space complexity**  
$O(1)$ - only use one extra variable.
