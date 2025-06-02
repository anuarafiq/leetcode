class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k == 0 or k == n: pass
        else:
            nums1 = []
            k %= n
            nums1 = nums[n-k:] + nums[:n-k]
            for i in range(n):
                nums[i] = nums1[i]
