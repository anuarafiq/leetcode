class Solution(object):
    def mergeAlternately(self, word1, word2):
        minimum = min(len(word1), len(word2))
        maximum = max(len(word1), len(word2))
        merged = ""
        for i in range(minimum):
            pointer1 = word1[i]
            pointer2 = word2[i]
            pair = pointer1 + pointer2
            merged += pair
        
        if len(word1) > len(word2):
            merged += word1[len(word2):]
        elif len(word1) < len(word2):
            merged += word2[len(word1):]

        return merged
