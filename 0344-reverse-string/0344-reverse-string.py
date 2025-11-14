class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low=0
        high=len(s)-1
        mid=(low+high)//2

        while low<=mid:
            s[low],s[high]=s[high],s[low]
            low+=1
            high-=1
        