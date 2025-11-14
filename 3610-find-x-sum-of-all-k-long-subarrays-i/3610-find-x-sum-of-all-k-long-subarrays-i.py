from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        result = []
        
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            count = Counter(window)
            
            # Sort by (-frequency, -value) so we get highest freq, then highest number
            sorted_items = sorted(count.items(), key=lambda a: (-a[1], -a[0]))
            
            # Take top x frequent numbers
            top_x = [num for num, freq in sorted_items[:x]]
            
            # Sum only occurrences of top x elements
            total = sum([num for num in window if num in top_x])
            result.append(total)
        
        return result

            