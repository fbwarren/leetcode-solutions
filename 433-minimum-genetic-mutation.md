# [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation)

**Main Idea**: We can imagine this problem as a graph where each valid gene string is a node, and mutations are the edges. Therefore, what the problem is *really* asking is for us to find the shortest path between the start node and end node. We use BFS to find the shortest path in a graph.

**Algorithm**  
We perform BFS using a queue starting at `start`. We use a tuple so that we can also keep track of the number of steps.  
For each character in a node, we change it to another gene letter and see if the new node is in `bank`.
If the new node is in `bank`, we add it to the queue.  
We keep doing this until we find a node that is equal to `end`, at which point we return the number of steps.  
If the queue becomes empty before we find `end`, then a path doesn't exist and we return -1.

```python
def minMutation(start, end, bank):
    queue = deque()
    queue.appendleft((start, 0))

    while queue:
        curr, steps = queue.pop()
        if curr == end:
            return steps
        for i in range(len(curr)):
            for c in "ACGT":
                mutation = curr[:i] + c + curr[i+1:]
                if mutation in bank:
                    queue.appendleft((mutation, steps+1))
                    bank.remove(mutation)

    return -1
```

**Time complexity**  
Since this problem is defined so that the gene strings have exactly 8 characters, and there are only 4 characters that the strings are built from, our BFS actually runs in constant time. The only part that *isn't* constant is searching `bank`, which takes up to $O(B)$ time where $B$ is the number of elements in the bank.  
However, if the strings could be length $n$ using $m$ characters, then we have $m^n$ possible strings.

**Space complexity**  
$O(1)$ since the input is specifically defined and limited.
