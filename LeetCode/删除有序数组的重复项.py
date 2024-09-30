class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list()
        length = 0
        for i in range(len(nums)):
            if not temp or nums[i] not in temp:
                temp.append(nums[i])
                length += 1
        nums = temp
        return length


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1
        return length


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        解释：这个算法的时间复杂度为 O(n)，另外 not in 的时间复杂度是O(n)
        """
        if not nums:
            return 0

        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 2, 3, 3, 3, 3, 5, 6, 6, 7, 9]))
    print(Solution().removeDuplicates([1, 1, 2]))
