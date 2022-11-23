def longestConsecutive(nums):
    longestStreak = 0
    numSet = set(nums)

    for num in numSet:
        if num - 1 not in numSet:
            currentStreak = 1
            currentNum = num

            while currentNum + 1 in numSet:
                currentStreak += 1
                currentNum += 1

            longestStreak = max(longestStreak, currentStreak)

    return longestStreak
