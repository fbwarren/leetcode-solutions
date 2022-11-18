# [235. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

**Main Idea**  
The root of a tree is only the lowest common ancestor if the two nodes are in different subtrees.  

**Algorithm**  
We perform dfs.  
If the current node is p or q, we simply return the node. This allows it to "bubble up", i.e. be returned all the way up to the top.  
Otherwise, if the current node isn't p or q, we proceed to the left and right subtrees. `left` and `right` will only take on values if p or q was found in those subtrees.  
If `left` and `right` both take on values, then that means `p` and `q` were in the left and right subtrees and so that means `root` is the common ancestor, so we return `root`.  
Otherwise, only one of `p` or `q` was found, so we return `left` or `right` accordingly.

```python
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return

    if root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right
```

**Time complexity**  
$O(n)$ since we visit each node up to once.

**Space complexity**  
$O(1)$ since we only use two constant size variables.
