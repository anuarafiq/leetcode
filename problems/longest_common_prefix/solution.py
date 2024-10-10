class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)

        if n == 1:
            return strs[0]
        if "" in strs:
            return ""
        
        i = 0
        minimum = float("inf")
        for word in strs:
            if len(word) < minimum:
                minimum = len(word)
        
        while i < minimum:
            for word in strs:
                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1

        return word[:i]
