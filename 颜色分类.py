def sortColors(nums):
    # 方法一
    i, j = 0, len(nums) - 1
    count = 0
    while i <= j:
        if nums[i] == 2:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1  # 数值 2 交换到尾部
        elif nums[i] == 1:
            nums[i] = 0  # 写入0
            count += 1  # 计算 1 的个数
            i += 1
        else:
            i += 1  # 0 只移动指针
    for index in range(j, j - count, -1):
        nums[index] = 1  # 写入 count 个 1
    # 方法二
    n = len(nums)
    ptr = 0
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    for i in range(ptr, n):
        if nums[i] == 1:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # 对方法一的优化
    i, j = 0, len(nums) - 1
    count0 = 0
    while i <= j:
        if nums[i] == 2:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1  # 数值 2 交换到尾部
            continue
        if nums[i] == 1:
            nums[i] = 0  # 写入 0
        else:
            count0 += 1  # 计算 1 的个数
        i += 1  # 0 只移动指针
    for index in range(count0, j + 1):
        nums[index] = 1  # 写入 count 个 1
        def sortColors(nums):
    # 最优算法
    n = len(nums)
    lt, gt, i = -1, n, 0
    while i < gt:
        if nums[i] == 0:
            lt += 1
            nums[lt], nums[i] = nums[i], nums[lt]
            i += 1
        elif nums[i] == 2:
            gt -= 1
            nums[gt], nums[i] = nums[i], nums[gt]
        else:
            i += 1
