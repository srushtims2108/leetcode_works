class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}
        for char in s:
            freqs[char]=freqs.get(char,0)+1
        for char in t:
            freqt[char]=freqt.get(char,0)+1
        return freqs==freqt
