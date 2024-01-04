from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        count = 0
        
        for value in num_count.values():
            if value == 1:
                return -1
            count += value // 3
            if value % 3:
                count += 1
            
        return count
            