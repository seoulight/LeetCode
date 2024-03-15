class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_product = 1
        zero_count = 0
        for n in nums:
            if n:
                non_zero_product *= n
            else:
                zero_count += 1
        answer = [0] * len(nums)
        for i, n in enumerate(nums):
            if n and not zero_count:
                answer[i] = non_zero_product // n
            elif not n and zero_count == 1:
                answer[i] = non_zero_product
        return answer