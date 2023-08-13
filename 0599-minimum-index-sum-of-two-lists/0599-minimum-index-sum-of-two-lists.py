class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        result = []
        minsum = len(list1) + len(list2) - 2
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if not result or i+j < minsum:
                        result = [list1[i]]
                        minsum = i + j
                    elif i + j == minsum:
                        result.append(list1[i])
        return result                        
                
        