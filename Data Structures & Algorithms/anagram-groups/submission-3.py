class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = dict() 
        # Loop through each word 
        for s in strs: 
        # Create a list of size 26, with 26 zeroes
            ls = [0] * 26  
        # loop through each letter, increment at index of list based on ascii value 
        # 97 = a, ord() 
            for char in s:
                ls[ord(char) - 97] += 1 
        # Now we have list, convert to tuple and add to a dictionary
            ls = tuple(ls) 
            if ls in resDict:
                resDict[ls].append(s)
            else:
                resDict[ls] = [s] 
        # go through dictionary and append to list, return result 
        res = [] 
        for val in resDict.values():
            r = []
            for word in val:
                r.append(word) 
            res.append(r)
        return res