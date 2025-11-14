class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        pattern= [""]* numRows
        row=0
        d=0
        for ch in s:
            pattern[row]+=ch
            
            if row==numRows-1:
                d=1
            elif row==0:
                d=0
            row+=1 if d==0 else -1
        
        return "".join(pattern)