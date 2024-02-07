from collections import Counter
from heapq import heapify, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        word_count = Counter(s)
        sorted_count = sorted(word_count.items(), key = lambda x:x[1], reverse = True)
        answer = ""
        for key, value in sorted_count:
            answer += key * value
        return answer
            
        