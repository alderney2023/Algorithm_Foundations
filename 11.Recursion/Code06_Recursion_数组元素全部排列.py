###########################################################################
# (从左往右， 选与不选)
#   给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
# 数组版： https://leetcode.cn/problems/permutations/
###########################################################################

# 打印一个字符串的全部排列
class Solution:
    def permute(self, nums) :
        if not nums or len(nums) == 0:
            return None
        res =[]
        self.process(nums, 0, res)
        return res

    def process(self, nums, i, res):
        if i == len(nums):
            res.append(nums.copy())
        else:
            s = set()
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    s.add(nums[j])
                    nums[i],nums[j] = nums[j],nums[i]
                    self.process(nums,i+1,res)
                    nums[i],nums[j] = nums[j],nums[i]




#---------------------------------------------------------------------------
def main():

    nums = [1,2,3]
    print(Solution().permute(nums)) 


if __name__ == "__main__":
    main()