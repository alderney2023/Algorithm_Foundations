###########################################################################
# 两个字符串的最长公共子序列的长度
#
# https://leetcode.com/problems/longest-common-subsequence/
#
#   暴力递归
#   动态规划
###########################################################################


#---------------------------------------------------------------------------------
#暴力递归

def longestCommonSubsequence1(s1, s2):
    if s1 == "" or len(s1) == 0 or \
       s2 == "" or len(s2) == 0:
        return 0
    return process1(s1, s2, len(s1)-1, len(s2)-1)

def process1(s1, s2, i, j):
    if i == 0 and j == 0:
        if s1[i] == s2[j]:
            return 1
        else:
            return 0
    elif i == 0:
        if s1[i] == s2[j]:
            return 1
        else:
            return process1(s1, s2, i, j-1)
    elif j == 0:
        if s1[i] == s2[j]:
            return 1
        else:
            return process1(s1, s2, i-1, j)

    else:
        p1 = process1(s1, s2, i-1, j)
        p2 = process1(s1, s2, i, j-1)
        p3=0
        if s1[i] == s2[j]:
            p3 = 1 + process1(s1, s2, i-1, j-1)
        return max(p1, p2, p3)


#---------------------------------------------------------------------------------
# 动态规划

def longestCommonSubsequence2(s1, s2):
    if s1 == "" or len(s1) == 0 or \
       s2 == "" or len(s2) == 0:
        return 0

    dp = [ [0] * (len(s2)) for _ in range(len(s1)) ]

    if s1[0]==s2[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0 
    for i in range(1,len(s1)):
        if s1[i] == s2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    for j in range(1,len(s2)):
        if s1[0] == s2[j]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]

    for j in range(1, len(s2)):
        for i in range(1, len(s1)):
            p1 = dp[i-1][j]
            p2 = dp[i][j-1]
            p3 = 0 
            if s1[i] == s2[j]:
                p3 = 1 + dp[i-1][j-1]
            dp[i][j] = max(p1,p2,p3)

    return dp[len(s1)-1][len(s2)-1]




#---------------------------------------------------------------------------------

def main():
    # lst1 = 'abc'
    # lst2 = 'def'

    lst1 = 'a1bc'
    lst2 = 'x1yz'
    print(longestCommonSubsequence1(lst1, lst2))
    print(longestCommonSubsequence2(lst1, lst2))
    

    
if __name__ == "__main__":
    main()