class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = []

        for l in logs:
            if l == '../':
                if path:
                    path.pop()
            elif l == './':
                continue
            else:
                path.append(l)

        return len(path)