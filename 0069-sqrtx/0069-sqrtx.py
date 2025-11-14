class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x 
        def sqrt(a,y):
            first=a
            last=y
            
            if first>last:
                return last
            mid=(first+last)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                return sqrt(mid+1,last)
            else:
                return sqrt(first,mid-1)
        return sqrt(1, x // 2)
    
