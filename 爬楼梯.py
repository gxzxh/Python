# 循环算法
def climbStairs(n):
    if n <= 2:
        return n
    pre, pre_pre, result = 2, 1, 0
    for i in range(3, n + 1):
        result = pre + pre_pre
        pre_pre = pre
        pre = result
    return result
