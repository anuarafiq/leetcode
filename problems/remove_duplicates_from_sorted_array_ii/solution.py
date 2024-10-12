class Solution(object):
    def removeDuplicates(self, nums):
        counter = 1
        n = len(nums)
        j = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[j] = nums[i]
                j +=1

        return j
        
        