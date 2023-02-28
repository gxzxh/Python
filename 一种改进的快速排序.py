from random import randint

# 原文地址：https://blog.csdn.net/insistGoGo/article/details/7785038
def insert_sort(arr, begin, end):
    """插入排序，begin，end为起始坐标和结束坐标，闭区间"""
    for index in range(begin + 1, end + 1):
        key = arr[index]
        current_index = index
        while current_index > begin and key < arr[current_index - 1]:
            arr[current_index] = arr[current_index - 1]
            current_index -= 1
        arr[current_index] = key
    return arr


def select_pivot_of_three(arr, low, high):
    """取待排序序列中low、mid、high三个位置，选中间数据作为枢轴
    arr[mid] <= arr[low] <= arr[high]
    low 位置上保存这三个位置的中间值
    分割时可以直接使用 low 位置的元素作为枢轴
    """
    mid = low + ((high - low) >> 1)
    # 目标: arr[mid] <= arr[high]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # 目标: arr[low] <= arr[high]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    # 目标: arr[low] >= arr[mid]
    if arr[mid] > arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    return arr[low]


def partition(arr, low, high):
    key = select_pivot_of_three(arr, low, high)
    first, last = low, high
    left, right = low, high
    left_len, right_len = 0, 0
    # 一次分割
    while low < high:
        while (high > low and arr[high] >= key):
            if arr[high] == key:  # 处理相等元素
                arr[right], arr[high] = arr[high], arr[right]
                right -= 1
                right_len += 1
            high -= 1
        arr[low] = arr[high]
        while high > low and arr[low] <= key:
            if arr[low] == key:
                arr[left], arr[low] = arr[low], arr[left]
                left += 1
                left_len += 1
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    # 一次快排结束
    # 把与枢轴 key 相同的元素移到枢轴最终位置周围
    j, i = first, low - 1
    while j < left and j < i:
        arr[i], arr[j] = arr[j], arr[i]
        i -= 1
        j += 1
    i, j = low + 1, last
    while j > right and i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return low - 1 - left_len, low + 1 + right_len


def quick_sort(arr, low, high):
    """改进的快速排序：\n
    优化一：当待排序序列的长度分割到一定大小后，使用插入排序。\n
    优化二：在一次分割结束后，可以把与 Key 相等的元素聚在一起。
            下次分割时，不用再对与 key 相等元素分割。\n
    优化三：通过三数取中（median-of-three）选取基准值。\n
    优化四：将函数尾部两次递归操作，优化为尾递归
    """
    if (high - low <= 10):
        insert_sort(arr, low, high)
        return arr
    while (low < high):
        pos1, pos2 = partition(arr, low, high)
        quick_sort(arr, low, pos1)
        low = pos2
    return arr