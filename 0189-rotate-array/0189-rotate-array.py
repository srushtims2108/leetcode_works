class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n<=1:
            return
        if k==0 or (n==k):
            return

        k %= n
        nums[:]=nums[-k:]+nums[:len(nums)-k]