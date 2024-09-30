class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_dict = {")": "(", "]": "[", "}": "{"}
        stack = list()
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i not in str_dict:
                stack.append(i)
            elif stack and stack[-1] == str_dict[i]:
                stack.pop()
            else:
                return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("([}}])"))
    print(Solution().isValid("({})"))
    print(Solution().isValid("(){}"))

# 力扣的官方题解
# class Solution:
#     def isValid(self, s: str) -> bool:
#         dic = {')': '(', ']': '[', '}': '{'}
#         stack = []
#         for i in s:
#             if stack and i in dic:
#                 if stack[-1] == dic[i]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(i)
#
#         return not stack
