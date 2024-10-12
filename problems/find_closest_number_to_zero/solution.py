class Solution(object):
    def findClosestNumber(self, nums):
        if len(nums) == 1: return nums[0]
        closest = nums[0]

        for num in nums[1:]:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest) and num > closest:
                closest = num

        return closest