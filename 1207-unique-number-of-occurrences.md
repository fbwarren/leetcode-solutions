# [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)

**Main Idea**  
Take advantage of the properties of sets.

**Algorithm**  
Count the number of time each number occurs.  
Then, check if the number of unique counts is equal to the number of unique numbers in `arr`.

```python
def uniqueOccurrences(self, arr: List[int]) -> bool:
    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    return len(set(counts.values())) == len(set(arr))
```

**Time complexity**  
$O(n)$ where $n$ is the number of elements in `arr`. 

**Space complexity**  
$O(n)$ where $n$ is the number of elements in `arr`.
