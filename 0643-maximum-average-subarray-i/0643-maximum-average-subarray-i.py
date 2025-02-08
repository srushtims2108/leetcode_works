

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_avg = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum)
        
        return max_avg / k
