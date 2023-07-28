class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=1
        left=0
        right=1
        if len(s)==0:
            return 0
        while right<len(s):
            if s[right] in s[left:right] and left<right:
                left+=1
            else:
                max_length = max(max_length, right - left + 1)
                right+=1
        return max_length