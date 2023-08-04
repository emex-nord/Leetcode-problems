class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefixSum = 0
        mp = {}
        for i in range(len(nums)):
            prefixSum += nums[i]
            prefixSum %= k

            if prefixSum == 0 and i:
                return True

            if prefixSum in mp:  # Found the required prefix sum 
                if i - mp[prefixSum] > 1:
                    return True  # check if at least 2 elements are there or not
            else:
                mp[prefixSum] = i

        return False
        