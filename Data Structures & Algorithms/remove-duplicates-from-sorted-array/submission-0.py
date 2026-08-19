"""
[1, 1, 2, 3, 4]
prev = 1 
j pointing to 1 
1 = 1, so remove the 1 that j is pointing too 
[1, 2, 3, 4] 
prev at 1 still, j now at 2 
not equal, so increment both 
prev at 2, j at 3, not equal so increment both 
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 1 
        k = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j) 
                continue
            else:
                i += 1 
                k += 1
            j += 1 
        return k

