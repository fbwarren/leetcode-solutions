# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Main Idea**  
Another classic recursion problem.  
If you're not comfortable with recursion, just remember to *assume* that your function is going to do what you want it to and treat it accordingly.  
In this case, if we know that `maxDepth()` will definitely return the max depth of any tree we give it, then we know that all we have to do is find the max depth of the left and right subtrees and return the greater of the two.  
Don't forget to add 1 for the parent!

**Algorithm**  

```python
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left, right) + 1
```

**Time complexity**  
$O(n)$ - we visit every node once

**Space complexity**  
$O(1)$ we don't use any data structures
