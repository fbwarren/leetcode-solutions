# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

**Main Idea**  
Making a couple optimizations to the brute force solution will get us an optimal solution. We can use a set to have constant time access to elements. The final part is to think about when we would want to go ahead and check an entire sequence.

**Algorithm**  
We create a set from `nums`.  
Then, we iterate through this set and we check if each number is part of a longer sequence by checking if `num-1` exists.  
If `num-1` doesn't exist, then we know `num` is the beginning of its sequence.  
So, we just count how many numbers are in the sequence, and update `longestStreak` accordingly.

```python
def longestConsecutive(nums):
    longestStreak = 0
    numSet = set(nums)

    for num in numSet:
        if num - 1 not in numSet:
            currentStreak = 1
            currentNum = num

            while currentNum + 1 in numSet:
                currentStreak += 1
                currentNum += 1

            longestStreak = max(longestStreak, currentStreak)

    return longestStreak
```

**Time complexity**  
$O(n)$ since sets have constant time lookups and we iterate through the set once.

**Space complexity**  
$O(n)$ for the set.
