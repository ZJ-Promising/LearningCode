"""
Topic:回文数
Description:给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        if temp == temp[::-1]:
            return "true"
        return "false"

if __name__=='__main__':
    Solution().isPalindrome(456)
