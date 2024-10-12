class Solution(object):
    def isSubsequence(self, s, t):
        if s == "" or s == t:
            return True
        if t == "":
            return False

        i = 0
        for letter in t:
            pointer = s[i]
            if letter == s[i]:
                i += 1
                if i == len(s):
                    return True
        
        return False