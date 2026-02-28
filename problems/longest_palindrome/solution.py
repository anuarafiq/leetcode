from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0

        for c in freq.keys():
            while freq[c] > 1:
                length += 2
                freq[c] -= 2
        
        leftover = sum(freq.values())
        return length + 1 if leftover >= 1 else length
