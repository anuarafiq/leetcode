class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for c in s:
            if stack:
                if c in pair and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
            
        return not stack
                
