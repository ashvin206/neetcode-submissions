"""
[1, 1, 2, 3, 4]
We start at 1 
next number is 1
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        while prev < len(nums) - 1:
            n = prev + 1 
            while n < len(nums) and nums[n] == nums[prev]:
                nums.pop(n)
                print(nums, prev, n)
            prev += 1 
        return len(nums)


