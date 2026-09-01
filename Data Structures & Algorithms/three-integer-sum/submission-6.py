"""
Sort nums to get 
nums = [-4, -1, -1, 0, 1, 2] 
-4, -1 and 2, but NOT big enough. move left pointer, FAIL 
-1, need 1, -1 and 2, that make 1, YAY, do we move both then idk 
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1 
            k = len(nums) - 1
            need = -nums[i]
            while j < k:
                if nums[j] + nums[k] == need: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < need:
                    j += 1 
                else:
                    k -= 1
        return res

