"""
nums = [1, 2, 4, 6] 
2 * 4 * 6 = 48
1 * 4 * 6 = 24 
1 * 2 * 6 = 12 
1 * 2 * 4 = 8 
[48, 24, 12, 8]

1 
1 * 1 
1 * 1 * 2
1 * 1 * 2 * 4 
[1, 1, 2, 8] prefix 
1 
1 * 6 
1 * 6 * 4 
1 * 6 * 4 * 2 
[48, 24, 6, 1] suffix 

[1, 1, 2, 8]
[1, 6, 24, 48] 
48 = 1 * 6 * 4 * 2 
24 = 1 * 6 * 4 
1 * 6 * 2 
8 = 1 * 2 * 4 
1 * 48 = 48 
1 * 24 = 24 
6 * 2 = 12 
8 * 1 = 8 
[48, 24, 12, 8] 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]
        suffixProduct = [1] 

        for i in range(len(nums) - 1):
            num = nums[i] 
            prefixProduct.append(prefixProduct[-1] * num) 
        for i in range(len(nums) - 1, 0, -1):
            num = nums[i] 
            suffixProduct.append(suffixProduct[-1] * num) 
        res = [] 
        for i in range(len(prefixProduct)):
            res.append(prefixProduct[i] * suffixProduct[len(prefixProduct) - 1 - i])
        return res

        