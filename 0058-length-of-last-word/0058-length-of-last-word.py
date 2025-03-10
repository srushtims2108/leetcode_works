class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        set=[]
        max_l=0
        set=s.split()
        return len(set[-1])   