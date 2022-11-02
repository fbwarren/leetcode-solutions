# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water)

**Main Idea**: This problem is simpler than it appears. It reminds me of [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).  
In both problems, the main idea behind the solution is recognizing that if you have to change the sides of the container (or the day you sell on in the case of problem 121), you should do so greedily.

**Algorithm**  
We use the following variables:  
`left, right`: pointers to the left and right side of a container  
`output`: keeps track of the size of our biggest container  

We start with the first and last column in the array and initialize `output`.  
Then, we check which column is shorter and move its corresponding pointer toward the other column. We update `output`.  
We keep doing this until the pointers have passed each other.  

```python
def maxArea(height):
    left, right = 0, len(height)-1
    output = 0
    while left < right:
        output = max(output, (right-left) * (min(height[left], height[right])))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return output
```

**Time complexity**  
$O(n)$

**Space complexity**  
$O(1)$
