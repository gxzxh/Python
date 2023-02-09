# 解法一
def moveZeroes(nums: list[int]) -> None:
    n = len(nums)
    if n <= 1:
        return
    j = 0
    for i in range(n):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    for index in range(j, n):
        nums[index] = 0
 # 解法二
 def moveZeroes(nums: list[int]) -> None:
    n = len(nums)
    if n <= 1:
        return
    # 两个指针i和j
    j = 0
    for i in range(len(nums)):
        # 当前元素!=0，就把其交换到左边，等于0的交换到右边
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
