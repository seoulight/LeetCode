class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique_char(s):
            char_set = set()
            for c in s:
                if c in char_set:
                    return False
                char_set.add(c)
            return True
    
        def dfs(arr: List[str], path: str, idx: int):
            if is_unique_char(path):
                nonlocal result
                result = max(result, len(path))
            if idx == len(arr) or not is_unique_char(path):
                return
            for i in range(idx, len(arr)):
                dfs(arr, path + arr[i], i + 1)
                
        result = 0
        dfs(arr, "", 0)
        return result
        
        
    
        
    