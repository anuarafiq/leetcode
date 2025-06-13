class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(filter(lambda x: x >= 0, nums))
        if not nums: return 1

        for i in range(1, max(nums) + 1):
            if i not in nums:
                return i
        
        return max(nums) + 1