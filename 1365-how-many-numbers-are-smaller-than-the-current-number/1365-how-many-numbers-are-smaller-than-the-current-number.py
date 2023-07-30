class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        counter = [0]*(max(nums) + 1)

        for i in nums:
            counter[i]+=1

        cum_sum = 0
        for i in range(len(counter)):
            val = counter[i]
            counter[i] = cum_sum 
            cum_sum += val

        for i, val in enumerate(nums):
            nums[i] = counter[val]
            
        return nums
