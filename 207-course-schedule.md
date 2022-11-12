# [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

**Main Idea**  
We're basically checking a graph for cycles.

**Algorithm**  
We start by setting up a hashmap that maps each class to its prerequisites and by setting up a set that will keep track of nodes (classes) we've already processed.  
Then,  we perform DFS on each class.  
During DFS, if we encounter a node we've already encountered before, then that means there's a cycle in the graph and we can return false.  
If the class has no prerequisites, then we can return true.  
Otherwise, we add it to our set of visited nodes and then perform DFS on all of its prerequisites.  
If all the prerequisites are found to have no cycles, then we have finished processing this class and we remove the class from the set of visited nodes since we are done with it. Also, we set its list of prerequisites to empty so that we don't perform extra work when we process the other remaining classes.  
Finally, after all classes are processed we can return true.

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}

        for prereq in prerequisites:
            hashmap[prereq[0]].append(prereq[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not hashmap[course]:
                return True
            visited.add(course)
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            hashmap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
```

**Time complexity**  
$O(V+E)$ where $V$ and $E$ are the vertices and edges of the graph.

**Space complexity**  
$O(V+E)$ because we create a hashmap for the classes, and the values in the hashmap are lists of the edges.
