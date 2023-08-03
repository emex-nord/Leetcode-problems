class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = 0
        lessthan = 0
        for n in nums:
            if n == target:
                count += 1
            if n < target:
                lessthan += 1

        result = []
        for i in range(count):
            result.append(lessthan)
            lessthan += 1

        return result