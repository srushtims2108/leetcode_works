class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max2=0
        c=0
        for i in gain:
            c+=i
            max2=max(max2,c)
        return max2