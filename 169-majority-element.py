def majorityElement(nums):          # Boyer-Moore majority vote algorithm
    candidate, count = nums[0], 1

    for num in nums:
        if num == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate, count = num, 1

    return candidate
