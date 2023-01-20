# [2244. Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/)

**Main Idea**  
Every number besides 1 can be factorized by 2 and 3.  
The only thing we have to look out for is numbers who have a remainder of 1 when divided by 3.

**Algorithm**  
We start by counting the occurrences of each task. (Use a hashmap/dictionary for efficiency).  
Then, for each task, we check if it's divisible by 3. If it is, the most efficient way to complete them is in sets of three, so we increase the output as such.  
Otherwise, the there's a remainder of 1 or 2 when we divide the task count by 3. It turns out that either way, the number of steps to complete this set of tasks will be one greater than the set of tasks divided by 3.  
This is because if the remainder is 2, then we will have to take a another step to do the remaining two tasks; Otherwise, if the the remainder is 1, then we actually want to do one less set of 3 tasks so that we have 4 tasks remaining instead, then finish the 4 tasks in two steps of two tasks.

```python
def minimumRounds(tasks: List[int]) -> int:
        output = 0
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        for count in counts:
            if counts[count] == 1:
                return -1
            if counts[count] % 3 == 0:
                output += counts[count] // 3
            else:
                output += (counts[count] // 3) + 1

        return output
```

**Time complexity**  
$O(n)$ where $n$ is the number of tasks. This is because we count the tasks, then do some constant time operations on the counts.

**Space complexity**  
$O(n)$ where $n$ is the number of tasks. This is because we use a dictionary whose size depends on the number of unique tasks.
