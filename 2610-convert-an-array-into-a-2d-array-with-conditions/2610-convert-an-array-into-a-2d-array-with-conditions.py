from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        max_count = max(num_count.values())
        result = [[] for _ in range(max_count)]
        for key in num_count.keys():
            for i in range(num_count[key]):
                result[i].append(key)
        return result