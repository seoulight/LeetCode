class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        divided = [nums[i - 3:i] for i in range(3, len(nums) + 1, 3)]
        for arr in divided:
            if arr[2] - arr[0] > k:
                return []
        return divided