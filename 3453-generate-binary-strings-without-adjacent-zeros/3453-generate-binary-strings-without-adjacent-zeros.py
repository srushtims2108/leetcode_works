class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def backtrack(path):
            if len(path)==n:
                res.append("".join(map(str, path)))

                return 
            if path[-1]==0:
                backtrack(path+[1])
            else:
                backtrack(path+[0])
                backtrack(path+[1])
        backtrack([0])
        backtrack([1])
        return res