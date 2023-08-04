class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]*len(nums)
        for i in range(len(nums)):
            prefixSum[i] = prefixSum[i -1] + nums[i]
            
        for i in range(len(nums)):
            leftSum = prefixSum[i] - nums[i]
            rightSum = prefixSum[-1] - prefixSum[i]
            if leftSum == rightSum:
                return i
        return -1