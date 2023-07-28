class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0  
        right = int(c**(0.5)) # this will make the code more efficient specially for larger values of c
        while right >= left:
            sum_of_squares = right**2 + left**2
            if sum_of_squares == c:
                return True
            elif sum_of_squares > c:
                right -= 1
            else:
                left += 1
        return False