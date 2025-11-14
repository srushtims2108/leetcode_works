class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=[]
        carry=0
        i=len(num1)-1
        j=len(num2)-1

        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(num1[i])
                i-=1
            if j>=0:
                total+=int(num2[j])
                j-=1
            carry=total//10
            res.append(str(total%10))
        return ''.join(res[::-1])