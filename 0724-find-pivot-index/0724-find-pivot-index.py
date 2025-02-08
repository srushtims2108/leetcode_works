class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s_l = sum(nums[:i])
            s_r = sum(nums[i+1:])
            if s_l==s_r:
                return i
        return -1