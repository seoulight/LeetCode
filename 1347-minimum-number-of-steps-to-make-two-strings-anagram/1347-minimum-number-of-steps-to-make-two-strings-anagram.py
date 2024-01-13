from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = defaultdict(int)
        
        for c in s:
            char_count[c] += 1
        
        for c in t:
            char_count[c] = char_count[c] - 1 if char_count[c] else char_count[c]
        answer = 0
        for count in char_count.values():
            answer += count
        return answer
            
            