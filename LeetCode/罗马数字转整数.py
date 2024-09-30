"""
 罗马数字转整数
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        romeDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if romeDict[s[i]] >= romeDict[s[i + 1]]:
                sum += romeDict[s[i]]
            else:
                sum -= romeDict[s[i]]

        return sum + romeDict[s[-1]]


if __name__ == '__main__':
    print(Solution().romanToInt("V"))
