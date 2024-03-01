from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        binary_count = Counter(s)
        return "1" * (binary_count['1'] - 1) + "0" * (binary_count['0']) + "1"