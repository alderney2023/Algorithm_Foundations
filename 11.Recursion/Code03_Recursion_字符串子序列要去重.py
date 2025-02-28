###########################################################################
# (从左往右， 选与不选)
# 打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
#
# https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a
###########################################################################

# 打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
class Solution:
    def NoDupSubSequences(self , s):
        # write code here
        if not s or len(s)==0:
            return [""]
        res = set()
        str = ""
        self.f2(s, 0, str, res)
        return list(res)

    def f2(self, s, i, str, res):
        if i == len(s):
            res.add(str)
            return
        self.f2(s, i+1, str+s[i], res)
        self.f2(s, i+1, str, res)


#---------------------------------------------------------------------------
def main():

    str = "122"
    print(Solution().NoDupSubSequences(str))
    # ['', 'cc', 'ac', 'a', 'c', 'acc']

if __name__ == "__main__":
    main()