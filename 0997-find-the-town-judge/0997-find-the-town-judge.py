from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(list)
        trust_person = set()
        
        if n == 1:
            return n
        for a, b in trust:
            trusted[b].append(a)
            trust_person.add(a)
            
        for person in trusted.keys():
            if len(trusted[person]) == n - 1 and person not in trust_person:
                return person
        return -1
                
        
            