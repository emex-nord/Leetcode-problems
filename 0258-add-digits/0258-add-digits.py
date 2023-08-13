class Solution:
    def addDigits(self, num: int) -> int:

        if len(str(num)) == 1:
            return num
        totalSum = 0
        for i in str(num):
            totalSum += int(i)
            
        return self.addDigits(totalSum)