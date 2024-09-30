"""
编写一个函数来查找字符串列表中的最长公共前缀。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str] 用于接收一个多个字符串的列表
        :rtype: str
        """
        min_len = strs.sort(key=lambda x: len(x))[0]  # 按照字符串的长度排序,找到最小长度的字符串
        res = ""
        i = 0
        while i < len(strs):
