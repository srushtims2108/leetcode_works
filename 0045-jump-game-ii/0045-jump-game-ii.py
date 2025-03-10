from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        far = 0
        count = 0
        end = 0
        
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            
            if i == end:
                count += 1
                end = far
                
                if end >= len(nums) - 1:
                    return count
        
        return count
