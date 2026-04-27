class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        result = [1, 1]
        for i in range(2, rowIndex+1):
            currRow = [1] + [result[i] + result[i-1] for i in range(1, len(result))] + [1]
            result = currRow

        return result