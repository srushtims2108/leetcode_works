class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a1=[]
        a2=[]
        res=[]
        for i,j in zip(A,B):
            a1.append(i)
            a2.append(j)
            res.append(len(list(set(a1).intersection(a2))))
        return res