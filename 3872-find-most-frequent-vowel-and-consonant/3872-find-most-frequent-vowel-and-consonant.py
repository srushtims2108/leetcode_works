class Solution:
    def maxFreqSum(self, s: str) -> int:
        val=(Counter(s))
        max_v=0
        max_c=0
        for key,value in val.items():
            if key in 'aeiou':
                max_v = max(max_v,value)
            else:
                max_c=max(max_c,value)
        return (max_v+max_c)