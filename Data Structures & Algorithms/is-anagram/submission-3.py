class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = dict()
        freqT = dict() 

        if len(s) != len(t): 
            return False 
        for i in range(len(s)):
            sChar = s[i]
            freqS[sChar] = freqS.get(sChar, 0) + 1 
            tChar = t[i] 
            freqT[tChar] = freqT.get(tChar, 0) + 1 
        return freqS == freqT 
