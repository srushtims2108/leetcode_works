class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        p_to_s={}
        s_to_p={}
        if len(pattern) != len(s):  # If lengths don't match, return False
            return False

        for char_p , char_s in zip(pattern,s):
            if (char_p in p_to_s and p_to_s[char_p]!=char_s) or \
                (char_s in s_to_p and s_to_p[char_s]!=char_p):
                return False
            p_to_s[char_p]=char_s
            s_to_p[char_s]=char_p
        return True