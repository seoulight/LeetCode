from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        answer = ""
        for o in order:
            if o in s_count:
                answer += o * s_count[o]
                del s_count[o]
        for remainder in s_count.keys():
            answer += remainder * s_count[remainder]
        return answer