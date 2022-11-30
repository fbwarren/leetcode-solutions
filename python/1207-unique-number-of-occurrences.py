def uniqueOccurrences(self, arr: List[int]) -> bool:
    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    return len(set(counts.values())) == len(set(arr))
