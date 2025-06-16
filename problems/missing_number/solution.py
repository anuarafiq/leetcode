class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        maxx = max(nums)
        nums_sum = (maxx * (maxx+1) // 2)

        if total == nums_sum:
            if nums.count(0) == 0:
                return 0
            return maxx + 1
        return nums_sum - total