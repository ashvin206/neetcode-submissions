"""
let's say we put nums in a set 
{2, 20, 4, 10, 3, 4, 5}
2 exists, we check if 1 exists, does not 
20 exists we check if 19 exists, does not 
4 exists, 3 exists, 2 exists so 3 
10 exists 9 does not 
5 exists, 4 exists ,3 exists, 2 exists, so 4 

Can try this logic first, then see if we can optimize it 

Works but is too slow 

The thing is, we are repeating a sequence 
start with 2 
when we get to 3, we see 3 and 2
when we get to 4, 4 3 2 
when we get to 5, 5 4 3 2 

Logically we need to skip the prior ones until we hit 5 

At 2, we already know because 1 does not exist
At 3, we know 2 exists, but we also know 4 exists, so we can skip that number
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums) 
        longest = 0 
        for i in range(len(nums)):
            num = nums[i] 
            m = 0
            if num + 1 in setNums:
                continue
            while num in setNums:
                m += 1 
                num -= 1 
            longest = max(longest, m)
        return longest
