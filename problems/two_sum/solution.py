class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[n] = i
        return None
 
