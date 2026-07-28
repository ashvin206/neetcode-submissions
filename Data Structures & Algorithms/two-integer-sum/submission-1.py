class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i in range(len(nums)):
            numsDict[nums[i]] = i 
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsDict and numsDict[diff] != i:
                return list((i, numsDict[diff]))