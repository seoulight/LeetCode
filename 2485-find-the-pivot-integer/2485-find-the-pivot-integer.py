class Solution:
    def pivotInteger(self, n: int) -> int:
        _sum = n * (n + 1) // 2
        x = math.sqrt(_sum)
        if x - math.ceil(x) == 0:
            return int(x)
        return -1