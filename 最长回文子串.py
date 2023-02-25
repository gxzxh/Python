# 方法一：动态规划
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    begin, max_len = 0, 1
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 枚举左边界，左边界的上限设置可以宽松一些
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = s[i + 1][L - 1]
            # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and L > max_len:
                max_len = L
                begin = i
    return s[begin : begin + max_len]

# 方法二：中心扩展算法
def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longestPalindrome(s):
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end + 1]

# 三：Manacher 算法
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return (right - left - 2) // 2

def longestPalindrome(s: str) -> str:
    end, start = -1, 0
    s = '#' + '#'.join(list(s)) + '#'
    arm_len = []
    right = -1
    j = -1
    for i in range(len(s)):
        if right >= i:
            i_sym = 2 * j - i
            min_arm_len = min(arm_len[i_sym], right - i)
            cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len)
        else:
            cur_arm_len = expand(s, i, i)
        arm_len.append(cur_arm_len)
        if i + cur_arm_len > right:
            j = i
            right = i + cur_arm_len
        if 2 * cur_arm_len + 1 > end - start:
            start = i - cur_arm_len
            end = i + cur_arm_len
    return s[start+1:end+1:2]
strs = "123aa321"
ans = longestPalindrome(strs)
print(ans)