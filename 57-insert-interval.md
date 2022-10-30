# [57. Insert Interval](https://leetcode.com/problems/insert-interval)

**Main Idea**: "Merging" two intervals that are overlapping means just setting the left to be the min of both intervals and the right to be the max of both.

**Algorithm**  
Basically, we iterate through the intervals and append all the ones that will occur before the new interval.  
Then, we deal with the intervals that intersect with the new interval by setting  
`newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]` as discussed in the main idea.  
Once we're past the intersecting intervals, we append the new interval. Finally, if there's any remaining intervals in `intervals`, we append those too.

```python
def insert(self, intervals, newInterval):
    output = []

    for i in range(len(intervals)):
        if newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            return output + [newInterval] + intervals[i:]
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

    output.append(newInterval)
    return output
```

**Time complexity**  
O(n) since the algorithm will always have to check all the intervals.  
**Space complexity**  
O(n) because output could have up to `len(intervals)+1` elements.
