"""
nums = [1, 2, 2, 3, 3, 3, 3] 
k = 2 
1 occurs 1 
2 occurs 2 
3 occurs 4 



"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict() 
        res = [] 
        # key = number, value = occurence 
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1 
        buckets = [[] for n in range(max(frequency.values()) + 1)] 
        for key, value in frequency.items():
            buckets[value].append(key)
        for i in range(-1, -1 * len(buckets), -1):
            bucket = buckets[i]
            for num in bucket:
                res.append(num)
                k -= 1 
                if k == 0:
                    return res
