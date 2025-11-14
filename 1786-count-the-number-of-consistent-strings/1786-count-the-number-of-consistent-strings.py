class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for w in words:
            if set(w) - allowed == set():
                ans += 1
        return ans