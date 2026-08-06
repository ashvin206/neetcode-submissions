"""
nums = [10, 9, 1, 1, 1, 2, 3, 1] 
Let's say we split this 
[10, 9, 1, 1] [1, 2, 3, 1] 
Split again
[10, 9] [1, 1] [1, 2] [3, 1]
Split
[10][9] [1][1] [1][2] [3][1]
Combine
[9,10] [1,1] [1,2] [1,3]
[1, 1, 9, 10][1, 1, 2, 3] 
[1, 1, 1, 1, 2, 3, 9, 10]
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, r, m):
            left = arr[l:m + 1]
            right = arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]: 
                    arr[i] = left[j]
                    j += 1 
                else:
                    arr[i] = right[k] 
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j] 
                i += 1 
                j += 1
            while k < len(right):
                arr[i] = right[k] 
                i += 1
                k += 1 
        def mergeSort(arr, l, r):
            m = (l + r) // 2 
            if l >= r:
                return 
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r) 
            merge(arr, l, r, m) 
        mergeSort(nums, 0, len(nums)-1)
        return nums


