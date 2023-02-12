# 方法一
def findKthLargest(nums, k):
    lo, hi = 0, len(nums) - 1
    k = len(nums) - k
    while lo <= hi:
        if hi - lo <= 1:
            if nums[hi] < nums[lo]:
                nums[hi], nums[lo] = nums[lo], nums[hi]
            return nums[k]
        pivot_data = nums[k]
        nums[k] = nums[hi]
        left, right = lo, hi
        while left < right:
            while nums[left] <= pivot_data and left < right:
                left += 1
            nums[right] = nums[left]
            while nums[right] >= pivot_data and left < right:
                right -= 1
            nums[left] = nums[right]
        nums[right] = pivot_data
        if right == k:
            return nums[k]
        if right < k:
            lo = right + 1
        else:
            hi = right - 1

# 方法二
# 采用快速排序方法，分成的数列左边大于右边
def findKthLargest(nums, k):
    def partition(nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j

    def quickSort(nums, l, r, k):
        if l >= r:
            return l
        p = partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return quickSort(nums, l, p - 1, k)
        else:
            return quickSort(nums, p + 1, r, k)

    n = len(nums)
    if (k > n):
        return
    index = quickSort(nums, 0, n - 1, k)
    return nums[index]
