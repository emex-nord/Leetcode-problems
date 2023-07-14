class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n % 2 == 0:
            return pow(x * x, n // 2)
        else:
            return x * pow(x * x, n // 2)
