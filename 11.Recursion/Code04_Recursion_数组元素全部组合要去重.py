###########################################################################
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的组合
# 答案 不能 包含重复的组合。返回的答案中，组合可以按 任意顺序 排列
# 注意其实要求返回的不是子集，因为子集一定是不包含相同元素的，要返回的其实是不重复的组合
# 比如输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# 测试链接 : https://leetcode.cn/problems/subsets-ii/
###########################################################################


class Solution:
    def subsetsWithDup(self, nums):
        if not nums or len(nums) == 0:
            return []
        nums = sorted(nums)
        res =[]
        subres = []
        self.process(nums, 0, subres, res)
        return res
    
    def process(self, nums, i, subres, res):
        if i == len(nums):
            res.append(subres)
        else:
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            self.process(nums, j, subres, res)    
            for k in range(j-i):
                self.process(nums, j, subres + nums[i:i+k+1], res)
    
#---------------------------------------------------------------------------
def main():

    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums)) 


if __name__ == "__main__":
    main()