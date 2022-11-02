# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

**Main Idea**  
It's doesn't make sense to include a subarray if its sum is negative, so don't.

**Algorithm**  
We loop through `nums`, calculating our current sum.  
If `currentSum` ever becomes negative, then we don't want to include our current subarray in our future calculations and therefore set `currentSum` to 0.  
We update our output at each step so that it tracks the max sum we've seen.

```python
def maxSubArray(self, nums):
    output = nums[0]
    currentSum = 0

    for num in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        output = max(output, currentSum)

    return output
```

**Time complexity**  
$O(n)$ since we loop through the array once.

**Space complexity**  
$O(1)$
