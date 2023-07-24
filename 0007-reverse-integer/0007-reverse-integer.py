from math import *
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        reversed=0
        num=abs(x)
        if num==0:
            n=1
        else:
            n=int(log10(num)+1)
        for i in range(n):
            last_digit=num%10
            num=(num-last_digit)//10
            reversed+=last_digit*10**(n-i-1)
        if reversed <= -(2**31)or reversed>=(2**31 - 1):
            return 0
        elif x>=0:
            return reversed
        else:
            return -1*reversed