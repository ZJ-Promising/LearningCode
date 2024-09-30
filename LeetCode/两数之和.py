"""
Topic:  两数之和
Description:给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target 的那两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建一个字典来存储数值和索引
        num_dict = {}
        # 遍历列表中的每一个元素
        for i, num in enumerate(nums):
            # 计算当前元素的补数
            complement = target - num
            # 检查补数是否在字典中
            if complement in num_dict:
                # 返回补数的索引和当前元素的索引
                return [num_dict[complement], i]
            # 将当前元素和索引存入字典
            num_dict[num] = i
