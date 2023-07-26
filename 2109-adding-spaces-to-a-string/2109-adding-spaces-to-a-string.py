class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        spaces=set(spaces)
        output=[]
        for index,char in enumerate(s):
            if index in spaces:
                output.append(" ")
            output.append(char)
        return "".join(output)            
