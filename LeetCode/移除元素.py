


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] != val:
                k += 1
                i += 1
            else:
                nums.pop(i)
        return k

if __name__ == "__main__":
    print(Solution().removeElement([12, 3, 3, 4, 44, 55, 5, 63, 3, 3],3 ))
