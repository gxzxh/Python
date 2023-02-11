 def removeDuplicates(nums):
    n = len(nums)
    i, j, index = 0, 1, 2
    while index < n:
        if not nums[i] == nums[j] == nums[index]:
            i += 1
            j += 1
            nums[j] = nums[index]
        index += 1
    return j + 1
