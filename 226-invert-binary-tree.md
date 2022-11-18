# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Main Idea**  
The *classic* recursion problem.  
Take the recursive leap of faith.

**Algorithm**  
This problem is easy to anyone that's familiar with recursion. If you're not familiar with recursion, or are struggling to fully digest it, it should comfort you to know that people say it's never used in practice.  
Anyways, when dealing with recursion, the best tip I can tell you is to take the "recursive leap of faith".  
What this means is that you should just believe that your function will do exactly what you want it to.  
For this example, this means to assume that `invertTree()` will *definitely* invert any tree you give it. If you have *faith* in `invertTree()`, then the problem becomes easier to solve.  
Why? Because now you know that you just have to switch your left and right childs' positions, and then invert their trees.  
Only other thing to think about is base case - i.e. when do we want to stop?  
In this case, we can't invert our tree if there is no tree. Therefore, if `root == None`, we just return nothing.

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
```

**Time complexity**  
$O(n)$ since we visit each node once

**Space complexity**  
$O(1)$ since we don't use any extra variables
