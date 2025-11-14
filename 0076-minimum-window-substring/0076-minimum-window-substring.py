from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        
        left, right = 0, 0
        formed = 0
        window_counts = {}
        min_len = float("inf")
        min_window = ""

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                window_counts[s[left]] -= 1
                if s[left] in dict_t and window_counts[s[left]] < dict_t[s[left]]:
                    formed -= 1

                left += 1  # Shrink the window

            right += 1  # Expand the window

        return min_window