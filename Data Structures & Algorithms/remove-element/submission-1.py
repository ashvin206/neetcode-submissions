class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        i = 0
        while i < len(nums): 
            num = nums[i] 
            if num == "_":
                break
            if val != num:
                print(val, num)
                k += 1 
            else:
                nums.pop(i)
                nums.append("_")
                i -= 1
            i += 1 
        print(k)
        return k
        