# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Main Idea**  
This is a hash map and sliding window problem.

**Algorithm**  
Iterate through the string while adding characters and their indices to the hash map.  
If you encounter a character that's already in the hash map and its index is after the start of the substring, move the start to right after that character's index.  
Update the output as you go. 

```python
def lengthOfLongestSubstring(s):
    hashMap = {}
    start, output = 0, 0

    for i, c in enumerate(s):
        if c in hashMap and hashMap[c] >= start:
            start = hashMap[c] + 1
        else:
            output = max(output, i - start + 1)
        hashMap[c] = i

    return output
```

**Time complexity**  
$O(n)$ since we iterate through the string once and hash map lookups and appends are constant time.

**Space complexity**  
$O(n)$ for the hash map.
