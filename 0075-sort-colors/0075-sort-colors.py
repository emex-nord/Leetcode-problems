class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counter_array = [0,0,0]
        for i in nums:
            counter_array[i] += 1
        
        target = 0
        for j in range(3):
            for i in range(counter_array[j]):
                nums[target] = j
                target += 1
            
        