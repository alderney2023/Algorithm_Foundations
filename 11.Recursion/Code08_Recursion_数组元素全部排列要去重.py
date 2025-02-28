###########################################################################
# (从左往右， 选与不选)
#   给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

# 数组版： https://leetcode.cn/problems/permutations-ii
###########################################################################


# 打印一个字符串的全部排列， 要求不要出现重复的排列
class Solution:
    def permuteUnique(self, nums):
        if not nums or len(nums)==0:
            return 
        res =[]
        self.f(nums, 0, res)
        return res

    def f(self, nums, i, res):
        if i == len(nums):
            res.append(nums.copy())
        else:
            s = set()
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    s.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    self.f(nums, i+1, res)
                    nums[i], nums[j] = nums[j], nums[i]       


#---------------------------------------------------------------------------
def main():

    nums = [1,1,2]
    print(Solution().permuteUnique(nums)) 


if __name__ == "__main__":
    main()