class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]] + [0] * (n - 1)
        # 1 * 2 * 3 * 4
        # (1 * 2 * 3 * 4) // (1 * 2) = (3 * 4)
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        answer = [0] * n
        for i in range(n):
            if nums[i] == 0:
                suffix = 1
                for j in range(i + 1, n):
                    suffix *= nums[j]
                answer[i] = prefix[i - 1] * suffix if i > 0 else suffix
            elif prefix[i] == 0:
                answer[i] = 0
            else:
                answer[i] = prefix[i - 1] * (prefix[-1] // prefix[i]) if i > 0 else prefix[-1] // prefix[i]
        return answer