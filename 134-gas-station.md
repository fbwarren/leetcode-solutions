# [134. Gas Station](https://leetcode.com/problems/gas-station/)

**Main Idea**: If our car's gas ever drops below 0, then we know that wherever we started from is an invalid cycle. However, we can also say that the stations between where we started and where we ran out of gas are also invalid start points, since there's no way we can start at one of those in-between stations and magically arrive at the same station but with more gas. This observation allows us to avoid a brute force solution.

**Algorithm**  
Variables:  
`start`: This is the output. Everytime we run out of gas, this is updated.  
`total`: Total gas used. This is basically the sum of the differences of each gas and cost element.  
`curr`: The current gas usage.  

Basically, we loop through all the stations and update `curr`.  
If `curr` becomes negative, we update `start` to be the next gas station because of the logic discussed in **main idea**.

```python
def canCompleteCircuit(gas, cost):
    start = 0
    total, curr = 0, 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]
        if curr < 0:
            start = i + 1
            curr = 0

    if total < 0:
        return -1
    return start
```

**Time complexity**  
$O(n)$ since we loop through the arrays once.

**Space complexity**  
$O(1)$
