class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + i
        for pivot in range(n, 0, -1):
            if prefix_sum[n] - prefix_sum[pivot - 1] == prefix_sum[pivot]:
                return pivot
        return -1