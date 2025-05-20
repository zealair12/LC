class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        vowel = "aeiou"
        result = 0
        vowCount = 0

        for r in range(n):
            if r >= k:
                if s[l] in vowel:
                    vowCount -= 1
                l += 1
            if s[r] in vowel:
                vowCount += 1
            
            result = max(result, vowCount)
        
        return result
