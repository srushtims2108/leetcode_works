class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f=[]
        for i in range(1,(n//2)+1):
            if (n%i==0):
                f.append(i);
        f.append(n)

        if k <= len(f):  
             return f[k - 1]  
        else:
            return -1
