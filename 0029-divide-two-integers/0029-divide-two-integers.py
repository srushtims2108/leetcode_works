class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        result = dividend // divisor

        if (dividend % divisor != 0) and ((dividend < 0) ^ (divisor < 0)):
            result += 1  

       
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
