# [39. Combination Sum](https://leetcode.com/problems/combination-sum)

**Main Idea**: DFS with backtracking

## Algorithm

In this solution, we use the recursive `dfs(candidates, target, combination)` function.  
`candidates` is the list of our candidates  
`target` is the current target  
`combination` is the current combination we have

While we are traversing the possible combinations, we keep track of our target value.  
The only possible way we have a valid combination is if `target == 0`.  
Otherwise, if `target < 0`, we need to backtrack.  
If the target is still positive, then we need to check if we can make a valid combination using the candidate numbers. We do this by making a recursive call for each candidate where the new target is equal to the old target minus the candidate.  
We pass `candidates[i:]` during these recursive calls to make sure we don't have repeated combinations.

## Time Complexity
Worst case, the depth of the tree will be `target`.  
This happens if there is a 1 in the candidates since we'd have to add 1 to itself `target` times.  
We can think of our decision tree as a binary tree, since node has 2 children: include the first candidate from the candidates it was given or don't include the first candidate.  
That makes our time complexity $O(2^{target})$.

```python
def combinationSum(self, candidates, target):
    output = []

    def dfs(candidates, target, combination):
        if target < 0:
            return
        if target == 0:
            output.append(combination)
            return
        else:
            for i in range(len(candidates)):
                dfs(candidates[i:], target-candidates[i], combination + [candidates[i]])

    dfs(candidates, target, [])
    return output
```