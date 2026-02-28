from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxx = -1
        majority = -1

        for n,f in freq.items():
            if f >= maxx:
                maxx = f
                majority = n

        return majority