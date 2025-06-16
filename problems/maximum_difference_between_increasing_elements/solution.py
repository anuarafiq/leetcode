class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = -1
        n = len(nums)

        for i in range(1, n):
            minn = min(nums[:i])
            diff = nums[i] - minn
            if diff > maxx:
                maxx = diff
        
        if maxx > 0: return maxx
        return -1