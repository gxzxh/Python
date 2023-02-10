def findDisappearedNumbers(nums):
    n = len(nums)
    for i in nums:
        x = (i - 1) % n
        nums[x] += n
    result = [i + 1 for i in range(n) if nums[i] <= n]
    return result
    
