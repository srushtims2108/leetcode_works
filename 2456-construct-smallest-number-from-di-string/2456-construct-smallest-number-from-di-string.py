class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=[str(i) for i in range(1,len(pattern)+2)]
        i=0
        while i<len(pattern):
            if pattern[i]=="D":
                j=i
                while j<len(pattern) and pattern[j]=="D":
                    j+=1
                res[i:j+1]=reversed(res[i:j+1])
                i=j
            else:
                i+=1
        return "".join(res)