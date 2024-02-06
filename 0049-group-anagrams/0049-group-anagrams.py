from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = list(s)
            sorted_s.sort()
            sorted_s = "".join(sorted_s)
            anagrams[sorted_s].append(s)
        return list(anagrams.values())