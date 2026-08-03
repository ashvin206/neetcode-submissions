class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        for i in range(len(strs[0])): # from 0 to length of first string
            for s in strs: # for each string 
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix