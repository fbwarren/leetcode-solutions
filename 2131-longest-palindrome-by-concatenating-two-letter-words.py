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
