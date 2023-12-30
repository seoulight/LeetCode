from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(int)
        for word in words:
            for c in word:
                char_count[c] += 1
        for count in char_count.values():
            if count % len(words) > 0:
                return False
        return True