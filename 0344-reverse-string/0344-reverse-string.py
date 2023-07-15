class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse(lst,start,stop):
            if stop-start>1:
                lst[start],lst[stop-1]=lst[stop-1],lst[start]
                return reverse(lst,start+1,stop-1)
            else:
                return lst
        reverse(s,0,len(s))
        return s
        