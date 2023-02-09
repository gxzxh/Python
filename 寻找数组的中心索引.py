def pivotIndex(nums: list[int]) -> int:
    totals = sum(nums)
    left, n = 0, len(nums)
    for i in range(n):
        totals -= nums[i]
        if left == totals:
            return i
        left += nums[i]
    return -1
