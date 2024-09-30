class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        dan_wei = 1
        j = 0
        for i in digits[::-1]:
            if j < len(digits):
                sum += int(i) * dan_wei
                dan_wei *= 10
                j += 1
        result = list()
        for i in str(sum+1):
            result.append(int(i))
        return result


if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 4, 5, 454, 6]))
    print(Solution().plusOne([1, 2, 4]))
    print(Solution().plusOne([4,3,4]))
