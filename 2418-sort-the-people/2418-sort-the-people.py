class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
    
        control=True
        while control:
            control=False
            for i in range(len(heights)-1):
                if heights[i+1]>heights[i]:
                    heights[i+1],heights[i]=heights[i],heights[i+1]
                    names[i+1],names[i]=names[i],names[i+1]
                    control=True
        return names
