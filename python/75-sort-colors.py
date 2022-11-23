def sortColors(self, nums):     # Dutch national flag problem
    redEnd, unsortedStart, blueStart = 0, 0, len(nums)-1

    while unsortedStart <= blueStart:
        if nums[unsortedStart] == 0:
            nums[redEnd], nums[unsortedStart] = 0, nums[redEnd]
            unsortedStart += 1
            redEnd += 1
        elif nums[unsortedStart] == 1:
            unsortedStart += 1
        else:
            nums[blueStart], nums[unsortedStart] = 2, nums[blueStart]
            blueStart -= 1

    return nums
