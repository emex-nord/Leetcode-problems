class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCounter=[0]*26
        pCounter=[0]*26
        letters= [chr(i) for i in range(ord('a'), ord('z')+1)]
        output=[]

        for i in p:
            pCounter[letters.index(i)]+=1

        for i in s[0:len(p)]:
            sCounter[letters.index(i)]+=1
            if sCounter==pCounter:
                output.append(0)

        for i in range(len(s)-len(p)):
            out=s[i]
            enter=s[i+len(p)]
            sCounter[letters.index(out)] -= 1
            sCounter[letters.index(enter)] +=1
            if sCounter == pCounter:
                output.append(i+1)
                
        return output
