def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefixes = [1] * len(nums)
    suffixes = [1] * len(nums)

    for i in range(1, len(nums)):
        prefixes[i] = prefixes[i-1] * nums[i-1]
        suffixes[len(nums)-i-1] = suffixes[len(nums)-i] * nums[-i]

    return [prefixes[i] * suffixes[i] for i in range(len(nums))]
