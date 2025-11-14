class Solution:
    def isHappy(self, n: int) -> bool:
        if not n:
            return False
        seen=set()
        def recur(nums):
            if nums==1:
                return True
            if nums in seen:
                return False
            seen.add(nums)
            total=sum(int(ch)**2 for ch in str(nums))
            return recur(total)
        return recur(n)