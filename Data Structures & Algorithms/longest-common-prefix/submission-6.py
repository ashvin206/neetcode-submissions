class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        smallestWord = strs[0]
        for i in range(1, len(strs)):
            s = strs[i] 
            if len(s) < len(smallestWord):
                smallestWord = s
        for i in range(len(smallestWord)):
            c = smallestWord[i] 
            for word in strs:
                if word[i] != c:
                    return prefix 
            prefix += c 
        return prefix