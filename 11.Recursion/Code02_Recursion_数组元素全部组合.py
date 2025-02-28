###########################################################################
# (从左往右， 选与不选)
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# https://leetcode.cn/problems/subsets
###########################################################################

class Solution:
    def subsets(self, nums):
        if not nums or len(nums) == 0:
            return []
        res = []
        subres = []
        self.process(nums, 0, subres, res)
        return res
    
    def process(self, nums, i, subres, res):
        if i == len(nums):
            res.append(subres)
        else:
            self.process(nums, i+1, subres, res)
            self.process(nums, i+1, subres+[nums[i]], res)


#---------------------------------------------------------------------------
def main():

    nums = [1,2,3]
    print(Solution().subsets(nums)) 


if __name__ == "__main__":
    main()