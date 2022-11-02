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
