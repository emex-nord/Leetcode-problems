class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        seeker=0
        placeholder=0

        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[seeker],nums[placeholder]=nums[placeholder],nums[seeker]
                placeholder+=1
                seeker+=1

            else:
                seeker+=1
                
        return nums