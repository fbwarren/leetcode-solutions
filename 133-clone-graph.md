# [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

**Main Idea**  
Recursive DFS, Hashmap

**Algorithm**  
We use depth first search (DFS) to traverse the list and we use a hashmap to keep track of our original and cloned nodes. For each node, we check if we've already cloned it by seeing if it's in the hashmap. If a clone exists, we just return that.  
If a clone doesn't exist, we clone it and put it in the hashmap, and then we update the clone's list of neighbors by appending the result of the recursive call on each neighbor.  
Finally, when we've processed all the neighbors, we return the new node.

```python
def cloneGraph(node: 'Node') -> 'Node':
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            copy = Node(node.val)
            hashmap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        hashmap = {}
        return dfs(node) if node else None
```

**Time complexity**  
$O(E+V)$ where $E$ and $V$ are the edges and vertices. 

**Space complexity**  
$O(V)$ since we use a hashmap to track the nodes.
