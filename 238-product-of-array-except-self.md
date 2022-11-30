# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

**Main Idea**  
Prefixes and suffixes.

**Algorithm**  
The product of an array except for an element can be thought of as the product of the prefix and suffix of that element.  
We can create an array for the prefixes and an array for the suffixes in one pass by multiplying each element in `nums` by the previous prefix and suffix.  
Once we've built the prefix array and the suffix array, our output is just the product of these two arrays.

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefixes = [1] * len(nums)
    suffixes = [1] * len(nums)

    for i in range(1, len(nums)):
        prefixes[i] = prefixes[i-1] * nums[i-1]
        suffixes[len(nums)-i-1] = suffixes[len(nums)-i] * nums[-i]

    return [prefixes[i] * suffixes[i] for i in range(len(nums))]
```

**Time complexity**  
$O(n)$ (where $n$ is the number of elements in `nums`) since we iterate through `nums` twice.

**Space complexity**  
$O(n)$ since we create two arrays that have $n$ elements.
