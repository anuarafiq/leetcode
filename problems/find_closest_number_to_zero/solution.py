class Solution(object):
    def findClosestNumber(self, nums):
        distance = []
        if not nums:
            return None
        
        closest = nums[0]

        for num in nums[1:]:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest) and num > closest:
                closest = num
        
        return closest