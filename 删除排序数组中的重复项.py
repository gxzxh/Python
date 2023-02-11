def removeDuplicates(nums) -> int:
    # 方法一单指针
    p = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[p]:
            p += 1
            nums[p] = nums[i]
    return p + 1
    # 方法二 双指针
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            if right != left:
                nums[left] = nums[right]
    return left + 1
