from sympy.utilities.codegen import Result


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        sum = self.ji_suan(a) + self.ji_suan(b)
        if sum ==0:
            return "0"
        while sum:
            result.append(sum % 2)
            sum //= 2
        jie=""
        for i in result[::-1]:
            jie+=str(i)
        return jie

    def ji_suan(self, number):
        sum = 0
        j = 0
        for i in number[::-1]:
            sum += int(i) * (2 ** j)
            j += 1
        return sum


if __name__ == '__main__':
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))
