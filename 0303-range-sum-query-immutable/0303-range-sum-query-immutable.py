class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)
        self.prefixSum = [0]*self.length
        
        for i in range(self.length):
            self.prefixSum[i] = self.prefixSum[i-1] + self.nums[i]
            
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)