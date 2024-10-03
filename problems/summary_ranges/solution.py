class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0 : return []
        if len(nums) == 1 : return [str(nums[0])]

        def appendToDomain(start, end):
            if start == end:
                domain.append(str(end))
            else:
                domain.append(str(start) + "->" + str(end))

        start = nums[0]
        domain = []

        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1] - 1:
                end = nums[i]
                appendToDomain(start, end)
                start = nums[i+1]
            end = nums[-1]
            
        appendToDomain(start, end)

        return domain
            