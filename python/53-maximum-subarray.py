def maxSubArray(self, nums):
    output = nums[0]
    currentSum = 0

    for num in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        output = max(output, currentSum)

    return output
