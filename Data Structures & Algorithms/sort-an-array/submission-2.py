"""

"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0 
        while l < len(nums) - 1:
            shift = False
            for i in range(l, len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    shift = True 
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp 
            if not shift:
                l += 1
        return nums