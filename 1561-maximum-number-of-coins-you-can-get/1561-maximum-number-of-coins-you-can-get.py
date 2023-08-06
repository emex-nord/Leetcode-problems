class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        i=0
        j = len(piles) - 2
        counter = 0
        while j > i:
            counter += piles[j]
            i += 1
            j -= 2

        return (counter)