# [2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

**Main Idea**:  
Count the number of words and their reverses that occur in the array. Repeated letters need to get a little special treatment.

**Algorithm**  
We make a Counter object out of the words. Counters are dictionaries where the values are the number of times a key occurs.  
Then we iterate through each word in the Counter.  
If a word is just a letter repeated twice, then we can add it to the center if it occurs and odd number of times. We can only have one center, so `center` is never more than 2. Also, if this word occurs more than once, then we have multiple pairs we can stick on both ends of a palindrome to build it, so we update `pairs`.  
If the word isn't just a double letter, then we find which of it and its reverse occur less often (to avoid double counting) and update `pairs`.  

```python
def longestPalindrome(words):
    wordSet = Counter(words)
    center, pairs = 0, 0

    for word in wordSet:
        reverse = word[1] + word[0]
        if word == reverse:
            if wordSet[word] % 2 != 0:
                center = 2
            pairs += wordSet[word] // 2 * 2
        else:
            pairs += min(wordSet[word], wordSet.get(reverse, 0))

    return 2 * pairs + center
```

**Time complexity**  
$O(n)$ because we potentially traverse `words` twice

**Space complexity**  
$O(n)$ for `wordSet`
