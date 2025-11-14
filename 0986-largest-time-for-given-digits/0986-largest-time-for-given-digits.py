from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        # generate all 24 permutations of 4 digits
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                total_minutes = hour * 60 + minute
                max_time = max(max_time, total_minutes)

        if max_time == -1:
            return ""

        # convert back to HH:MM format
        hh = max_time // 60
        mm = max_time % 60
        return f"{hh:02d}:{mm:02d}"
