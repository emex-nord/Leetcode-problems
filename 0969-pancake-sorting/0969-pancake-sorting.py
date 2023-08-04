class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(arr,k):
            i = 0
            while k > i:
                arr[k],arr[i] = arr[i],arr[k]
                k -= 1
                i += 1

        output = []
        j = len(arr) - 1
        while j > 0:
            maximum = max(arr[0:j + 1])
            index = arr.index(maximum)
            if index == j:
                j -= 1
                pass
            elif index == 0:
                output.append(j + 1)
                flip(arr,j)
                j -= 1
            else:
                output.extend([index + 1,j + 1])
                flip(arr,index)
                flip(arr,j)
                j -= 1
        return output