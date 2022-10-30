# [169. Majority ELement](https://leetcode.com/problems/majority-element)

**Main Idea**: I think solving this in linear time is probably easy enough for most people. The tricky part is solving this using constant space.

## First Algorithm

This solution just iterates through the numbers while keeping track of their frequency in a hashmap.

```python
def majorityElement(nums):
    hashmap = {}

    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
        if hashmap.get(num, 0) > len(nums)/2:
            return num
```

## Complexity

**Time complexity:** O(n) where n == len(nums), since at worst we'll have to check each element.  
**Space complexity:** O(n) because of the hash map.

## Better Algorithm

This solution is known as the [Boyer-Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm).  
It takes advantage of the fact that a strict majority is guaranteed to exist.  
Because of this guarantee, we only have to keep track of a single `candidate` value and its `count`.  
Looking at the code below, we can see that since majority element, by definition, occurs more often than any other element, it will always end up being the final `candidate`.

```python
def majorityElement(nums):
    candidate, count = nums[0], 1

    for num in nums:
        if num == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate, count = num, 1

    return candidate
```

## Complexity

**Time complexity:** O(n) since we iterate through all numbers.  
**Space complexity:** O(1) because we only have `candidate` and `count`.
