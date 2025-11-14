class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = None
        second = None
        for index, value in enumerate(nums):
            if value == target:
                if first is None:
                    first = index
                second = index  # always update second to the latest 

        if first is None:
            return [-1, -1]
        return [first, second]
