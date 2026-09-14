class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in numsDict and i != numsDict[target - nums[i]]:
                return [i, numsDict[target - nums[i]]]