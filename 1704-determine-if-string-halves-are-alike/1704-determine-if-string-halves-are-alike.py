class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = "aeiou";
        def count_vowel(string: str) -> int:
            count = 0
            string = string.lower()
            for s in string:
                if s in vowel:
                    count += 1
            return count
        mid = len(s) // 2
        return count_vowel(s[:mid]) == count_vowel(s[mid:])
            