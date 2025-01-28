class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag=0
        for i in range(len(nums)):
            if nums[i]==target:
               flag=1
               break
        if flag==1:
            return i
        else:
            return -1

        