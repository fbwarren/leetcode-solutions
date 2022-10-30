# [75. Sort Colors](https://leetcode.com/problems/sort-color)

**Main Idea**: The easiest way is to count the number of 0's, 1's, and 2's.  
However, If we want to solve this problem with only one pass, we have to use the approach found [here](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

**First Algorithm**  
Here, we count the number of 0's, 1's, and 2's then alter `nums` in-place using these counts.

```python
def sortColors(nums):
    counts = [0, 0, 0]

    for num in nums:
        counts[num] += 1

    i = 0
    for num, count in enumerate(counts):
        while count:
            nums[i] = num
            count -= 1
            i += 1

    return nums
```

**Time complexity:** O(n), but it takes two passes so it's more like O(2n)  
**Space complexity:** O(1) since `counts` is our only auxiliary data structure and it's always the same size

**Second Algorithm**  
The key to this algorithm is that we are looping through `nums` while maintining a [loop invariant](https://en.wikipedia.org/wiki/Loop_invariant).  
A loop invariant is simply some condition that we make sure is always true between loop iterations.  
To me, it seems that a loop invariant is useful in the same way the [recursive leap of faith](https://people.eecs.berkeley.edu/~bh/pdf/v1ch08.pdf) is - we don't have to think to hard about why it works as long as we *assume* it does.  
In this case, we initialize 3 pointers that represent the end of the red section, the beginning of the unsorted section, and the start of the blue section.  
Becuase of our invariant, we always know that only red is before the end of the red section, only white is between the end of the red section and the beginning of the unsorted section, and that only blue is after the start of the blue section, then we can easily sort the unsorted stuff.  
So, we sort each unsorted item by putting it in the appropriate section, and adjusting the pointers accordingly.

```python
def sortColors(self, nums):
    redEnd, unsortedStart, blueStart = 0, 0, len(nums)-1

    while unsortedStart <= blueStart:
        if nums[unsortedStart] == 0:
            nums[redEnd], nums[unsortedStart] = 0, nums[redEnd]
            unsortedStart += 1
            redEnd += 1
        elif nums[unsortedStart] == 1:
            unsortedStart += 1
        else:
            nums[blueStart], nums[unsortedStart] = 2, nums[blueStart]
            blueStart -= 1
    
    return nums
```

**Time complexity:** O(n), one pass  
**Space complexity:** O(1) since we only use 3 integer variables
