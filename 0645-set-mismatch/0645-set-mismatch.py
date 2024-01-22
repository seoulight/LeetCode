class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        curr = 2 if 1 == nums[0] else 1
        reput = nums[0]
        for i in range(1, n):
            if nums[i] == curr:
                curr += 1
            if nums[i - 1] == nums[i]:
                reput = nums[i]
        return [reput, curr]
            