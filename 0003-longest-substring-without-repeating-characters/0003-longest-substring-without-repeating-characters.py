class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        c = 0
        l = []
        seen = set()
        i = 0
        
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                c += 1
                j += 1
            else:
                seen.remove(s[i])
                c -= 1
                i += 1
            
            l.append(c)
        
        return max(l) if l else 0
