from collections import defaultdict, deque

class Solution:        
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        prime2index = defaultdict(list)
        index2prime = defaultdict(list)
        for i, n in enumerate(nums):
            temp = n
            for j in range(2, int(n ** 0.5) + 1):
                if temp % j == 0:
                    prime2index[j].append(i)
                    index2prime[i].append(j)
                while temp % j == 0:
                    temp //= j
            if temp > 1:
                prime2index[temp].append(i)
                index2prime[i].append(temp)
                
        q = deque([0])
        visited_index = [False] * len(nums)
        visited_prime = []
        while q:
            curr = q.popleft()
            visited_index[curr] = True
            for prime in index2prime[curr]:
                if prime not in visited_prime:
                    visited_prime.append(prime)
                    for index in prime2index[prime]:
                        if not visited_index[index]:
                            q.append(index)
            
        return False not in visited_index
        