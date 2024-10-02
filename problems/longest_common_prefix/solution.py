class Solution(object):
    def longestCommonPrefix(self, strs):
        if "" in strs :
            return ""
        
        if len(strs) == 1:
            return strs[0]

        minimum = float("inf")
        for word in strs:
            if len(word) < minimum:
                minimum = len(word)

        i = 0
        while i < minimum:
            for word in strs:
                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1
        
        return word[:i]