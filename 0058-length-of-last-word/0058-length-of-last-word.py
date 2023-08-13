class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        while i+1:
            if s[i] == " " and length:
                return length
            else:
                if s[i] != " ":
                    length += 1
                i -= 1
              
        return length