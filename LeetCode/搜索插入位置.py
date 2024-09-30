class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                nums.insert(i, target)
                return i
        nums.append(target)
        return i + 1
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(len(list(map(str,s.split()))[-1]))

if __name__ == "__main__":
    print(Solution().searchInsert([1, 2, 3, 4, 56, 767877, 6575677676], 6))
    print(Solution().searchInsert([1, 2, 3, 4, 56, 767, 877, 999], 100000))
    print(Solution().searchInsert([1, 2, 3, 4, 56, 767, 877, 999], 2))

