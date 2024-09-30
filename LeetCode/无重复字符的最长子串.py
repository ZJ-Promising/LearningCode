class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0  # 定义长度
        for i in range(len(s)):
            temp = 0  # 定义临时变量存储字符串的长度
            for j in range(i, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    temp += 1
            length = length if length > temp else temp
        return length






if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
