class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1)
        m = len(word2)
        minimum = min(n, m)

        merged = ""
        for i in range(minimum):
            pointer1 = word1[i]
            pointer2 = word2[i]
            pair = pointer1 + pointer2
            merged += pair

        if n < m:
            merged += word2[n:]
        else:
            merged += word1[m:]  

        return merged