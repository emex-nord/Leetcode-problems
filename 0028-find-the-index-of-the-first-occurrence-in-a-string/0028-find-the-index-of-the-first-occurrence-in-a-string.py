class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index=-1
        for i in range(len(haystack)-len(needle)+1):
            if needle[0]==haystack[i] and index==-1:
                index=i
                for j in range(1,len(needle)):
                    if needle[j]==haystack[i+j]:
                        continue
                    else:
                        index=-1
            if index==i:
                break
        return index


            