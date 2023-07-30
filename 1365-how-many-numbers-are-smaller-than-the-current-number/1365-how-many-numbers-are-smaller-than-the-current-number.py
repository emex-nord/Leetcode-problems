class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        
        for i, val in enumerate(nums):
            nums[i] = sorted_nums.index(val) 
        
        return nums